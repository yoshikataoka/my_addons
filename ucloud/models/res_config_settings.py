# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_system_name = fields.Char('System Name', help="Setup System Name,which replace Odoo",
                                  default='uCloud', config_parameter='app_system_name')
    app_show_lang = fields.Boolean('Show Quick Language Switcher',
                                   help="When enable,User can quick switch language in user menu",
                                   config_parameter='app_show_lang')
    app_show_debug = fields.Boolean('Show Quick Debug', help="When enable,everyone login can see the debug menu",
                                    config_parameter='app_show_debug')
    app_show_documentation = fields.Boolean('Show Documentation', help="When enable,User can visit user manual",
                                            config_parameter='app_show_documentation')
    # 停用
    app_show_documentation_dev = fields.Boolean('Show Developer Documentation',
                                                help="When enable,User can visit development documentation")
    app_show_support = fields.Boolean('Show Support', help="When enable,User can vist your support site",
                                      config_parameter='app_show_support')
    app_show_account = fields.Boolean('Show My Account', help="When enable,User can login to your website",
                                      config_parameter='app_show_account')
    app_show_enterprise = fields.Boolean('Show Enterprise Tag', help="Uncheck to hide the Enterprise tag",
                                         config_parameter='app_show_enterprise')
    app_show_share = fields.Boolean('Show Share Dashboard', help="Uncheck to hide the Odoo Share Dashboard",
                                    config_parameter='app_show_share')
    app_show_poweredby = fields.Boolean('Show Powered by Odoo', help="Uncheck to hide the Powered by text",
                                        config_parameter='app_show_poweredby')
    group_show_author_in_apps = fields.Boolean(string="Show Author in Apps Dashboard", implied_group='app_odoo_customize.group_show_author_in_apps',
                                               help="Uncheck to Hide Author and Website in Apps Dashboard")
    module_odoo_referral = fields.Boolean('Show Odoo Referral', help="Uncheck to remove the Odoo Referral")

    app_documentation_url = fields.Char('Documentation Url', config_parameter='app_documentation_url')
    app_documentation_dev_url = fields.Char('Developer Documentation Url', config_parameter='app_documentation_dev_url')
    app_support_url = fields.Char('Support Url', config_parameter='app_support_url')
    app_account_title = fields.Char('My Odoo.com Account Title', config_parameter='app_account_title')
    app_account_url = fields.Char('My Odoo.com Account Url', config_parameter='app_account_url')
    app_enterprise_url = fields.Char('Customize Module Url(eg. Enterprise)', config_parameter='app_enterprise_url')
    app_ribbon_name = fields.Char('Show Demo Ribbon', config_parameter='app_ribbon_name')
    app_navbar_pos_pc = fields.Selection(string="Navbar PC", selection=[
        ('top', 'Top(Default)'),
        ('bottom', 'Bottom'),
        # ('left', 'Left'),
    ], config_parameter='app_navbar_pos_pc')
    app_navbar_pos_mobile = fields.Selection(string="Navbar Mobile", selection=[
        ('top', 'Top(Default)'),
        ('bottom', 'Bottom'),
        # ('left', 'Left'),
    ], config_parameter='app_navbar_pos_mobile')

    def set_module_url(self):
        sql = "UPDATE ir_module_module SET website = '%s' WHERE license like '%s' and website <> ''" % (self.app_enterprise_url, 'OEEL%')
        try:
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass

