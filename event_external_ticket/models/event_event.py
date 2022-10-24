from odoo import fields, models


class Event(models.Model):
    _inherit = "event.event"

    is_external = fields.Boolean(default=False)
    external_registration_page = fields.Char()
