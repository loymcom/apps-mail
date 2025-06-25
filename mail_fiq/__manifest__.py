# Copyright 2025 FIQ as
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "FIQ Mail Apps",
    "author": "FIQ as, Odoo Community Association (OCA)",
    "website": "https://fiq.no",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": [

        # OCA
        "mail_composer_cc_bcc", # git@github.com:norlinhenrik/oca-mail/tree/18.0-fix-mail_mail-email_to ### beta/mail
        "mail_optional_follower_notification", # git@github.com:odoonz/mail.git ### beta/.mail_optional_follower_notification
        "mail_quoted_reply",
        "mail_tracking",

        # Loym/FIQ
        "mail_force_email_notification_compose",
        "mail_message_security",
        "mail_never_autofollow", # consider mail_optional_autofollow https://github.com/OCA/mail/pull/29

        # Wishlist
        # - mail_quoted_reply_all
        # - User setting: Handle important notifications in Email, otherwise in Odoo
    ],
    "data": [
        "security/mail_message_security.xml",
    ],
}
