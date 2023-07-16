from odoo import fields, models


class TwilioPhoneNumber(models.Model):
    _name = 'twilio.phone.number'
    _description = 'Twilio Phone Number'

    name = fields.Char(string="Friendly Name")
    phone_number = fields.Char(string="Phone Number")
    related_account_id = fields.Many2one('res.company', string="Related Account")

    _sql_constraints = [
        ('uniq_phone_number', 'unique(phone_number)',
         'You already have this phone number used in other record')]