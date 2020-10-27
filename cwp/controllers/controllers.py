# -*- coding: utf-8 -*-
# from odoo import http


# class Cwp(http.Controller):
#     @http.route('/cwp/cwp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cwp/cwp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cwp.listing', {
#             'root': '/cwp/cwp',
#             'objects': http.request.env['cwp.cwp'].search([]),
#         })

#     @http.route('/cwp/cwp/objects/<model("cwp.cwp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cwp.object', {
#             'object': obj
#         })
