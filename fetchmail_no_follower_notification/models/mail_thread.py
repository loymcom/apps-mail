import logging
import traceback

from odoo import models
from odoo.http import request


_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        """
        Do not notify followers if the context indicates that the fetchmail cron is running.
        """
        if request and hasattr(request, 'httprequest') and request.httprequest:
            _logger.warning("request.params: " + str(request.params))
            _logger.warning("request.httprequest.headers: " + str(request.httprequest.headers))
        # fetchmail_cron_running is not reliable, but default_fetchmail_server_id should be
        if self.env.context.get("default_fetchmail_server_id"):
            _logger.warning("_notify_get_recipients: fetchmail_no_follower_notification due to fetchmail_cron_running.")
            _logger.warning("_notify_get_recipients traceback:")
            _logger.warning(traceback.format_stack())
            return []
        else:
            _logger.warning("_notify_get_recipients: context = " + str(self.env.context))
            _logger.warning("_notify_get_recipients traceback:")
            _logger.warning(traceback.format_stack())
            return super()._notify_get_recipients(message, msg_vals, **kwargs)
