# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CallCenter(http.Controller):
    @http.route('/callcenter/status', methods=['POST'], type='http', auth='public', csrf=False)
    def status(self, phone, status, **kw):
        
        # print(phone)
        phone = '+' + phone
        phone = phone.replace(" ", "")
        # print(phone)
        phoneRec = request.env['callcenter.phone.list'].sudo().search([('phone', '=', phone)], limit=1)
        
        print(phoneRec)
        match status:
            case 'answered':
                phoneRec.sudo().write({'status':'answered'})
            case 'busy':
                phoneRec.sudo().write({'status':'busy'})
            case 'no_answer':
                phoneRec.sudo().write({'status':'no_answer'})
            case 'failed':
                phoneRec.sudo().write({'status':'failed'})
            case 'transferred':
                phoneRec.sudo().write({'status':'transferred'})
        # phoneRec.sudo().write({'status':'draft'})
        return 'Update Success!'
        # return None

    @http.route('/callcenter/recording', methods=['POST'], type='http', auth='public', csrf=False)
    def recording(self, Called, RecordingUrl, CallStatus, From, **kw):
        
        print(Called)
        Called = '+' + Called
        phone = Called.replace(" ", "")
        print(RecordingUrl)
        
        phoneRec = request.env['callcenter.phone.list'].sudo().search([('phone', '=', phone)], limit=1)
        print(phoneRec)
        phoneRec.sudo().update({'call_log_ids':[(0, 0, {'link':RecordingUrl, 'callStatus':CallStatus, 'to':From})]})
        
        return "Recording updated!"