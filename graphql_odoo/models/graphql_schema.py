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

    @api.model
    def _register_hook(self):
        """
        To build dynamic graphql schema when module is loaded.
        """
        super()._register_hook()
        if not hasattr(self.env.registry, '_graphql_schema'):
            self.env.registry._graphql_schema = {}
        for rec in self.search([]):
            model_name = rec.ir_model_id.model.replace('.', '_')
            attrs = {}
            for field in rec.ir_model_fields_ids:
                field_type = self._get_graphene_field_type(field.ttype)
                attrs[field.name] = field_type()
            graphql_model = type(
                model_name, (graphene.ObjectType,), attrs
            )

            def resolver(root, info):
                result = []
                model_fields = info.context['fields']
                for r in info.context['records']:
                    obj = graphql_model()
                    for f in model_fields:
                        setattr(obj, f, getattr(r, f, None))
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
            schema = graphene.Schema(query=query_model)
            self.env.registry._graphql_schema[rec.name] = schema

    @api.constrains('name', 'active', 'ir_model_id', 'ir_model_fields_ids')
    def _update_schema(self):
        """
        Update registry with latest schema.
        """
        self._register_hook()

    @staticmethod
    def _get_graphene_field_type(odoo_type):
        return {
            'char': graphene.String,
            'text': graphene.String,
            'boolean': graphene.Boolean,
            'integer': graphene.Int,
            'float': graphene.Float,
        }.get(odoo_type, graphene.String)
