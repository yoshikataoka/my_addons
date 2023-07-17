from odoo import fields, models, api
from twilio.rest import Client

class PhoneList(models.Model):
    _name = 'callcenter.phone.list'
    _rec_name = "phone"
    _description = 'List of phone numbers to Call'
    
    phone = fields.Char('Phone', required=True)
    status = fields.Selection([('draft', 'Draft'), 
                              ('scheduled', 'Scheduled'),
                              ('answered','Answered'),
                              ('busy','Busy'),
                              ('no_answer','No Answer'),
                              ('failed','Call Failed'),
                              ('transferred','Transferred'),], string="Status")
    call_log_ids = fields.One2many('callcenter.call.log','phone_id', string='Call Logs')
    call_log_count = fields.Integer(string='Count of Logs', compute='_compute_account_type')
    
    @api.depends('call_log_ids')
    def _compute_account_type(self):
        if self.call_log_ids:
            self.call_log_count = len(self.call_log_ids)
        else:
            self.call_log_count = 0
        

    
class CallSchedule(models.Model):
    _name = 'callcenter.call.schedule'
    _rec_name = "name"
    _description = 'Schedule to make call'
    
    name = fields.Char('Schedule Name', required=True)
    phone_ids = fields.Many2many('callcenter.phone.list', string="Scheduled Phone#")
    time = fields.Float('Duration in hours ')
    repeat = fields.Boolean('Repeat Schedule?')
    flow_id = fields.Many2one('callcenter.call.flow', string='Flow')
  
    # @api.one
    def make_call(self):
        if self.flow_id:
            flowId = self.flow_id.flow_id
        else:
            flowId = ''
        if self.phone_ids:
            for phone in self.phone_ids:
                twilio_account_sid = self.env.company.twilio_account_sid
                twilio_auth_token = self.env.company.twilio_auth_token
                client = Client(twilio_account_sid, twilio_auth_token)
                execution = client.studio.v2.flows(flowId).executions.create(to=phone.phone, from_='+12192667888')
                phone.sudo().update({'call_log_ids':[(0, 0, {'execution_sid':execution.sid})]})
        # print(execution.sid)
        
                    
class CallFlow(models.Model):           
    _name = 'callcenter.call.flow'
    _rec_name = "name"
    _description = "Twilio Flow"
    
    name = fields.Char()
    flow_id = fields.Char('Flow Id')
    
class CallLog(models.Model):
    _name = 'callcenter.call.log'
    _rec_name = "create_date"
    _description = "Call logs"
    
    phone_id = fields.Many2one('callcenter.phone.list')
    link = fields.Char('Recording Link')
    to = fields.Char('Used Phone#')
    callStatus = fields.Char('Call Status')
    execution_sid = fields.Char('Execution SID')
    call_sid = fields.Char('Call SID')
    # start_datetime = fields.Datetime('Start DateTime')
    