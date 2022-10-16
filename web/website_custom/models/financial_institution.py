# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class financial__institution(models.Model):
    _name = 'financial_institution'
    _inherit = 'mail.thread'


    name = fields.Char("Financial Institution")
    code = fields.Char("Code / Commercial Register")
    advertising_number = fields.Integer("Advertising number")
    License_Num = fields.Char("License No  Master Username")
    delegate_name = fields.Many2one("res.users", string="Delegate Name")
    phone = fields.Char(related="delegate_name.mobile", string="mobile number")
    password = fields.Char("Password")
    email = fields.Char(related="delegate_name.email", string="Email")
    logo = fields.Image()
    s=fields.Many2one("sale.order")



    def get_quotation(self):
        self.ensure_one()
        return {
            'name': _('sale.order'),
            'view_mode': 'kanban,form',
            'views': [(False, 'kanban'), (False, 'form')],
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref("sale.view_sale_order_kanban").id,
            'domain': [('offer', '=', self.name)]
        }






