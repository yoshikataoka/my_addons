# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CallCenter(http.Controller):
    @http.route('/callcenter/init', methods=['POST'], type='http', auth='public', csrf=False)
    def init(self, phone, execution_sid, callSid, **kw):
        print(phone)
        if '+' in phone:
            phone = phone.replace(" ", "")
        else:
            phone = '+' + phone
            phone = phone.replace(" ", "")
        print(phone)
        phoneLog = request.env['callcenter.call.log'].sudo().search([('execution_sid', '=', execution_sid)], limit=1)
        print(phoneLog)
        
        phoneLog.sudo().write({'call_sid':callSid, 'to':phone})
        
        return 'Update Success!'
    
    @http.route('/callcenter/status', methods=['POST'], type='http', auth='public', csrf=False)
    def status(self, execution_sid, status, **kw):
        
        phoneLog = request.env['callcenter.call.log'].sudo().search([('execution_sid', '=', execution_sid)], limit=1)
        phoneLog.sudo().write({'callStatus':status})
        
        return 'Update Success!'
        