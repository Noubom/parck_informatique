# -*- coding: utf-8 -*-
# from odoo import http


# class ParckInformatique(http.Controller):
#     @http.route('/parck_informatique/parck_informatique/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parck_informatique/parck_informatique/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parck_informatique.listing', {
#             'root': '/parck_informatique/parck_informatique',
#             'objects': http.request.env['parck_informatique.parck_informatique'].search([]),
#         })

#     @http.route('/parck_informatique/parck_informatique/objects/<model("parck_informatique.parck_informatique"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parck_informatique.object', {
#             'object': obj
#         })
