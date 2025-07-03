from odoo import fields, models, api


class PropertyType(models.Model):
    _name = 'real_estate.property_type'
    _description = 'Real Estate Property Type'

    name = fields.Char()
