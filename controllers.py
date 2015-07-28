# -*- coding: utf-8 -*-
from openerp import http

# class MrcPaymentCharge(http.Controller):
#     @http.route('/mrc_payment_charge/mrc_payment_charge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrc_payment_charge/mrc_payment_charge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrc_payment_charge.listing', {
#             'root': '/mrc_payment_charge/mrc_payment_charge',
#             'objects': http.request.env['mrc_payment_charge.mrc_payment_charge'].search([]),
#         })

#     @http.route('/mrc_payment_charge/mrc_payment_charge/objects/<model("mrc_payment_charge.mrc_payment_charge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrc_payment_charge.object', {
#             'object': obj
#         })