# -*- coding: utf-8 -*-
from odoo import api, fields, models
import graphene


class GraphQLSchema(models.Model):
    """
    Model to save GraphQL schemas.
    """
    _name = 'graphql.schema'
    _description = 'GraphQL Schema'

    name = fields.Char(required=True)
    active = fields.Boolean('Active', default=True)
    ir_model_id = fields.Many2one('ir.model', 'Model')
    ir_model_fields_ids = fields.Many2many(
        'ir.model.fields',
        string='Fields',
        domain='[("model_id", "=", ir_model_id)]'
    )

    # @api.constrains
    # check if the model is added for many2one and many2many fields
    # check for compute field

    def _register_hook(self) -> None:
        """
        To build dynamic graphql schema when module is loaded.
        """
        super()._register_hook()
        self._build_graphql_schemas()

    def _build_graphql_schemas(self) -> None:
        """
        (Re)build every active schema and store it on the registry.
        """
        schemas = {}
        for rec in self.search([('ir_model_id', '!=', False)]):
            model_name = rec.ir_model_id.model.replace('.', '_')
            attrs = {}
            for field in rec.ir_model_fields_ids:
                field_type = self._get_graphene_field_type(field.ttype)
                attrs[field.name] = field_type()
            graphql_model = type(
                model_name, (graphene.ObjectType,), attrs
            )

            def resolver(root, info, _model=graphql_model):
                result = []
                model_fields = info.context['fields']
                for r in info.context['records']:
                    obj = _model()
                    for f in model_fields:
                        value = getattr(r, f, None)
                        # Odoo returns False for empty non-boolean fields
                        if value is False and r._fields[f].type != 'boolean':
                            value = None
                        setattr(obj, f, value)
                    result.append(obj)
                return result

            query_model = type(
                'Query',
                (graphene.ObjectType,),
                {
                    model_name: graphene.List(graphql_model),
                    f'resolve_{model_name}': resolver,
                }
            )
            schemas[rec.name] = graphene.Schema(query=query_model)
        self.env.registry._graphql_schema = schemas

    @api.constrains('name', 'active', 'ir_model_id', 'ir_model_fields_ids')
    def _update_schema(self) -> None:
        """
        Update registry with latest schema.
        """
        self._build_graphql_schemas()

    @staticmethod
    def _get_graphene_field_type(odoo_type: str):
        return {
            'char': graphene.String,
            'text': graphene.String,
            'boolean': graphene.Boolean,
            'integer': graphene.Int,
            'float': graphene.Float,
        }.get(odoo_type, graphene.String)
