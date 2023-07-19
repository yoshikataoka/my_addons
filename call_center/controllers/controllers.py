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
        
        match status:
            case 'answered':
                phoneLog.sudo().write({'callStatus':'answered'})
            case 'busy':
                phoneLog.sudo().write({'callStatus':'busy'})
            case 'no_answer':
                phoneLog.sudo().write({'callStatus':'no_answer'})
            case 'failed':
                phoneLog.sudo().write({'callStatus':'failed'})
            case 'transferred':
                phoneLog.sudo().write({'callStatus':'transferred'})
        # phoneRec.sudo().write({'status':'draft'})
        return 'Update Success!'
        # return None

    # @http.route('/callcenter/recording', methods=['POST'], type='http', auth='public', csrf=False)
    # def recording(self, CallSid, RecordingUrl, **kw):
        
    #     print(RecordingUrl)
        
    #     phoneLog = request.env['callcenter.call.log'].sudo().search([('call_sid', '=', CallSid)], limit=1)
    #     print(phoneRec)
    #     phoneLog.sudo().write({'link':'RecordingUrl'})
        
    #     return "Recording updated!"