# -*- coding: utf-8 -*-
from odoo import http


class Ldc(http.Controller):
    @http.route('/home/', auth='public')
    def index(self, **kw):
        Clientes = http.request.env['ldc.clientes']
        return http.request.render('ldc.index', {
            'clientes': Clientes.search([])
        })

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
