from odoo import models, fields, api

class RealEstateProperty(models.Model):
    _name = 'real_estate.property'
    _description = 'Real Estate Property'

    name = fields.Char('Title',required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Available From', copy=False, default=fields.Date.today)
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], 'Garden Orientation')
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ],'Status', default='new', copy=False)
    property_type_id = fields.Many2one('real_estate.property_type', string='Property Type')
    #customer_id = fields.Many2one('res.partner', string='Customer')
    property_multiplier = fields.Float(string='Price Multiplier', related='property_type_id.price_multiplier', readonly=True)
    owner_id = fields.Many2one('res.partner', string='Owner', copy=False)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', copy=False)