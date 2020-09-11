# -*- coding: utf-8 -*-
# from odoo import http


# class Cvp(http.Controller):
#     @http.route('/cvp/cvp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cvp/cvp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cvp.listing', {
#             'root': '/cvp/cvp',
#             'objects': http.request.env['cvp.cvp'].search([]),
#         })

#     @http.route('/cvp/cvp/objects/<model("cvp.cvp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cvp.object', {
#             'object': obj
#         })
