from odoo import api, fields, models

#Nomor 1
class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Service Team'

    #a
    name = fields.Char(string='Name', required=True)
    #b
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader', required=True)
    #c
    team_members = fields.Many2many(comodel_name='res.users', string='Team Members')