# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

try:
    from twilio.rest import Client
except ImportError:
    _logger.error('Cannot import twilio dependencies', exc_info=True)

class ResCompany(models.Model):
    _inherit = 'res.company'

    twilio_account_sid = fields.Char(string="Twilio Account SID")
    twilio_auth_token = fields.Char(string="Twilio Auth Token")
    twilio_api_key = fields.Char(string="Twilio API Key")
    twilio_api_secret = fields.Char(string="Twilio API Secret")
    twilio_phone_number_ids = fields.One2many('twilio.phone.number', 'related_account_id')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
