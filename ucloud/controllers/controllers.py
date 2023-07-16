# -*- coding: utf-8 -*-
# from odoo import http


# class Ucloud(http.Controller):
#     @http.route('/ucloud/ucloud', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ucloud/ucloud/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ucloud.listing', {
#             'root': '/ucloud/ucloud',
#             'objects': http.request.env['ucloud.ucloud'].search([]),
#         })

#     @http.route('/ucloud/ucloud/objects/<model("ucloud.ucloud"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ucloud.object', {
#             'object': obj
#         })
