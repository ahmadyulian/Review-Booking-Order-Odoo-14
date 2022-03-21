# -*- coding: utf-8 -*-
# from odoo import http


# class Review-booking-order-odoo14(http.Controller):
#     @http.route('/review-booking-order-odoo14/review-booking-order-odoo14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/review-booking-order-odoo14/review-booking-order-odoo14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('review-booking-order-odoo14.listing', {
#             'root': '/review-booking-order-odoo14/review-booking-order-odoo14',
#             'objects': http.request.env['review-booking-order-odoo14.review-booking-order-odoo14'].search([]),
#         })

#     @http.route('/review-booking-order-odoo14/review-booking-order-odoo14/objects/<model("review-booking-order-odoo14.review-booking-order-odoo14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('review-booking-order-odoo14.object', {
#             'object': obj
#         })
