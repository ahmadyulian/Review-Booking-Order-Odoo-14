from odoo import api, fields, models

#Nomor 2
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #a
    is_booking_order = fields.Boolean(string='Is Booking Order')
    #b
    team = fields.Many2one(comodel_name='service.team', string='Team')
    #c
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader')
    #d
    team_members = fields.Many2many(comodel_name='res.users', string='Team Members')
    #e
    booking_start = fields.Datetime(string='Booking Start')
    #f
    booking_end = fields.Datetime(string='Booking End')