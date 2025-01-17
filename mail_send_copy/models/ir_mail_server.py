# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from email.utils import COMMASPACE

from odoo import api, models


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    @api.model
    def send_email(self, message, *args, **kwargs):
        do_not_send_copy = self.env.context.get("do_not_send_copy", False)
        bcc_email = self.env['ir.config_parameter'].sudo().get_param('mail.bcc')
        if not bcc_email:
            bcc_email = message["From"]
        if not do_not_send_copy:
            if message["Bcc"]:
                message["Bcc"] = message["Bcc"].join(COMMASPACE, bcc_email)
            else:
                message["Bcc"] = bcc_email
        return super().send_email(message, *args, **kwargs)
