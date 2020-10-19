# -*- coding: utf-8 -*-
# from odoo import http


# class Prb(http.Controller):
#     @http.route('/prb/prb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prb/prb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prb.listing', {
#             'root': '/prb/prb',
#             'objects': http.request.env['prb.prb'].search([]),
#         })

#     @http.route('/prb/prb/objects/<model("prb.prb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prb.object', {
#             'object': obj
#         })
