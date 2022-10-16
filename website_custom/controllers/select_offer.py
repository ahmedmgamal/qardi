import datetime
from odoo import fields
from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class Odoooffer(http.Controller):
    @http.route(['/my/orders/<int:order_id>'], type='http', auth="public", website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        print(kw)
        offer = kw.get('offer')
        print(offer)