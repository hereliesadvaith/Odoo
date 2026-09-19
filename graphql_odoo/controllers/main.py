# -*- coding: utf-8 -*-
from graphql import parse
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
        return request.make_json_response({'hello': 'hi'})

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
            schemas = getattr(request.env.registry, '_graphql_schema', {})
            schema = schemas.get(fields[0])
            if schema is None:
                return request.make_json_response(
                    {'errors': [{'message': f'Unknown schema: {fields[0]}'}]},
                    status=404
                )
            # Add search_read and domain limit
            records = request.env[self.camel_to_dot(fields[0])].sudo().search(
                [])
            result = schema.execute(
                values.get('query'),
                context_value={'records': records, 'fields': [
                    self.camel_to_snake(f) for f in fields[1:]]},
            )
            if result.errors:
                return request.make_json_response(
                    {'errors': [e.formatted for e in result.errors]},
                    status=400
                )
            if result.data:
                return request.make_json_response(result.data)
            return request.make_response(
                'Something went wrong. Please try again.',
                status=500
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
