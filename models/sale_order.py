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

    #Nomor 6D #oofonchange
    @api.onchange('team')
    def _onchange_team(self):
        search = self.env['service.team'].search([('id', '=', self.team.id)])
        
        team_members = []
        
        for team in search:
            team_members.extend(members.id for members in team.team_members)
            self.team_leader = team.team_leader.id
            self.team_members = team_members

    #Nomor 6E
    def button_check(self):
        for check in self:
            workorder = self.env['work.order'].search(
                [('team_leader', 'in', [workorder.id for workorder in self.team_members]),
                 ('team_members', 'in', [self.team_leader.id]),
                 ('team_leader', '=', self.team_leader.id),
                 ('team_members', 'in', [workorder.id for workorder in self.team_members]),
                 ('state', '!=', 'cancelled'),
                 ('planned_start', '<=', self.booking_end),
                 ('planned_end', '>=', self.booking_start)
                ], limit=1
            )

            #Nomor 6E I 1
            if workorder:
                raise ValidationError('Team already has work order during that period on SOXX')
            #Nomor 6E I 2
            else:
                raise ValidationError('Team is available for booking')
    
    #Nomor 6F
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for check in self:
            workorder = self.env['work.order'].search(
                ['|', '|', '|',
                 ('team_leader', 'in', [workorder.id for workorder in self.team_members]),
                 ('team_members', 'in', [self.team_leader.id]),
                 ('team_leader', '=', self.team_leader.id),
                 ('team_members', 'in', [workorder.id for workorder in self.team_members]),
                 ('state', '!=', 'cancelled'),
                 ('planned_start', '<=', self.booking_end),
                 ('planned_end', '>=', self.booking_start)
                ], limit=1
            )

            #Nomor 6F I
            if workorder:
                raise ValidationError('Team is not available during this period, already booked on SOXX.Please book on another date.')
            return res

    def action_work_order_create(self):
        workorder = self.env['work.order']
        
        for search in self:
            workorder.create([{'bo_references': search.id,
                            'team': search.team.id,
                            'team_leader': search.team_leader.id,
                            'team_members': search.team_members.ids,
                            'planned_start': search.booking_start,
                            'planned_end': search.booking_end}])