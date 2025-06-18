import logging

from odoo import models


_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        """
        Do not notify followers if the context indicates that the fetchmail cron is running.
        """
        if self.env.context.get("fetchmail_cron_running"):
            _logger.info("_notify_get_recipients: fetchmail_no_follower_notification due to fetchmail_cron_running.")
            return []
        else:
            _logger.info("_notify_get_recipients: super()")
            return super()._notify_get_recipients(message, msg_vals, **kwargs)
