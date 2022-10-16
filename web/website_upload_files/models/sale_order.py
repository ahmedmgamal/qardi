# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attachment_count = fields.Integer('Attachment Count',
                                      compute='_compute_attachment_count')

    def _compute_attachment_count(self):
        for rec in self:
            attachments = self.env['ir.attachment'].search_count(
                [('res_model', '=', 'sale.order'), ('res_id', '=', rec.id)])
            rec.attachment_count = attachments

    def action_show_attachments(self):
        return {
            'name': _('Attachments'),
            'view_mode': 'kanban,form',
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'domain': [('res_model', '=', 'sale.order'), ('res_id', '=', self.id)]
        }
