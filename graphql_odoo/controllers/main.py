# -*- coding: utf-8 -*-
from graphql import parse
from graphql_server import format_error_default
from odoo.http import Controller, request, route
import json
import logging
import re

_logger = logging.getLogger(__name__)


class GraphQLController(Controller):
    """
    Controller for GraphQL.
    """
    @route('/api', type='http', auth='none', csrf=False,
           methods=['GET'], cors='*'
           )
    def api_data(self, **kw):
        """
        Fetch data
        """
        data = request.env['res.partner'].sudo().search([])
        for rec in data:
            print(rec.read())
        print(data)
        return request.make_response(
            json.dumps({
                'hello': 'hi'
            }),
            status=200
        )

    @route('/graphql', type='http', auth='none', csrf=False,
           methods=['POST'], cors='*'
           )
    def graphql(self, **kw):
        """
        GraphQL endpoint.
        """
        try:
            body = request.httprequest.data.decode('utf-8')
            values = json.loads(body)
            document = parse(values.get('query'))
            operation = document.definitions[0]
            fields = self.extract_fields(operation.selection_set)
            schema = request.env.registry._graphql_schema.get(fields[0])
            # Add search_read and domain limit
            records = request.env[self.camel_to_dot(fields[0])].sudo().search(
                [])
            result = schema.execute(
                values.get('query'),
                context_value={'records': records, 'fields': [
                    self.camel_to_snake(f) for f in fields[1:]]},
            )
            output = {}
            if result.errors:
                output['res'] = json.dumps(
                    [format_error_default(e) for e in result.errors]
                )
                output['status'] = 400
            elif result.data:
                output['res'] = json.dumps(result.data)
                output['status'] = 200
            else:
                output['res'] = 'Something went wrong. Please try again.'
                output['status'] = 500
            return request.make_response(
                output.get('res'),
                status=output.get('status')
            )
        except Exception as e:
            _logger.warning(e)
            return request.make_response(
                'Something went wrong. Please try again.',
                status=500
            )

    def extract_fields(self, selection_set):
        fields = []
        for selection in selection_set.selections:
            if hasattr(selection, 'name'):
                fields.append(selection.name.value)
            if selection.selection_set:
                fields.extend(self.extract_fields(selection.selection_set))
        return fields

    def camel_to_dot(self, name):
        # Insert a dot before uppercase letters, then lowercase everything
        parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', name)
        return '.'.join(part.lower() for part in parts)

    def camel_to_snake(self, name):
        s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
        s2 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1)
        return s2.lower()
