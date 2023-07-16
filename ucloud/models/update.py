# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
import logging

import requests
import werkzeug.urls

from ast import literal_eval
from odoo import api, release, SUPERUSER_ID, models
from odoo.exceptions import UserError
from odoo.models import AbstractModel
from odoo.tools.translate import _
from odoo.tools import config, misc, ustr

_logger = logging.getLogger(__name__)


class EnterpriseHack(models.AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model

    def update_notification(self, cron_mode=True):
        
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('database.expiration_date', '2099-12-31 00:00:00')
        set_param('database.expiration_reason', 'svip will not expired.')
        set_param('database.enterprise_code', 'eduninef')
        
        return True
