# -*- coding: utf-8 -*-
# from odoo import http


# class Ldc(http.Controller):
#     @http.route('/ldc/ldc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ldc/ldc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ldc.listing', {
#             'root': '/ldc/ldc',
#             'objects': http.request.env['ldc.ldc'].search([]),
#         })

#     @http.route('/ldc/ldc/objects/<model("ldc.ldc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ldc.object', {
#             'object': obj
#         })
