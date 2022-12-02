# -*- coding: utf-8 -*-
# from odoo import http


# class My-addon(http.Controller):
#     @http.route('/my-addon/my-addon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my-addon/my-addon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my-addon.listing', {
#             'root': '/my-addon/my-addon',
#             'objects': http.request.env['my-addon.my-addon'].search([]),
#         })

#     @http.route('/my-addon/my-addon/objects/<model("my-addon.my-addon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my-addon.object', {
#             'object': obj
#         })
