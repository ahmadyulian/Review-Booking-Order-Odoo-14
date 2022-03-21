from odoo import api, fields, models, _

#Nomor 3
class WorkOrder(models.Model):
    _name = 'work.order'
    _description = 'New Description'

    #a
    wo_number = fields.Char(string='Wo Number', required=True, default=lambda self: _('New'))
    #b
    bo_references = fields.Many2one(comodel_name='sale.order', string='BO Reference', readonly=True)
    #c
    team = fields.Many2one(comodel_name='service.team', string='Team', required=True)
    #d
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader', required=True)
    #e
    team_members = fields.Many2many(comodel_name='res.users', string='Team Members', required=True)
    #f
    planned_start = fields.Datetime(string='Planned Start', required=True)
    #g
    planned_end = fields.Datetime(string='Planned Start', required=True)
    #h
    date_start = fields.Datetime(string='Date Start', readonly=True)
    #i
    date_end = fields.Datetime(string='Date End', readonly=True)
    #j
    state = fields.Selection(
        string='State', 
        selection=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')],
        default='pending'
        )
    #k
    note = fields.Text(string='Note')
    