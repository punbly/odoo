from odoo import fields, models, api


class AirlineAlliance(models.Model):
    _name = 'airline_db.alliance'
    _description = 'Airline Alliance'

    name = fields.Char(required=True)
    website = fields.Char()

class Airline(models.Model):
    _name = 'airline_db.airline'
    _description = 'Airline'

    name = fields.Char(required=True)
    airline_id = fields.Many2one('res.partner', string='Airline', required=True)
    country_id = fields.Many2one(related='airline_id.country_id', string='Country', readonly=True)
    iata_member = fields.Boolean(string='IATA Membership')
    alliance = fields.Many2one('airline_db.alliance', string='Alliance')
    service_type = fields.Selection([
        ('low_cost','Low Cost'),
        ('premium_charter','Premium Charter'),
        ('standard','Standard'),
        ('domestic','Domestic'),
        ('charter','Charter'),])
    flag_carrier = fields.Boolean(string='Flag Carrier')
    aircraft_no = fields.Integer(string='Number of Aircraft')
    revenue_total = fields.Float(string='Total Revenue')
    revenue_ancillary = fields.Float(string='Ancillary Revenue')
