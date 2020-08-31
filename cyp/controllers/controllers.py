# -*- coding: utf-8 -*-
# from odoo import http


# class Cyp(http.Controller):
#     @http.route('/cyp/cyp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cyp/cyp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cyp.listing', {
#             'root': '/cyp/cyp',
#             'objects': http.request.env['cyp.cyp'].search([]),
#         })

#     @http.route('/cyp/cyp/objects/<model("cyp.cyp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cyp.object', {
#             'object': obj
#         })
