# -*- coding: utf-8 -*-
from odoo import http


from odoo.addons.website_sale.controllers.main import WebsiteSale,TableCompute
from odoo.http import request
import json

class WebsiteSale(WebsiteSale):

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        print("DD>D>D>D>",kw)
        product_brand_id=kw.get('product_brand_id')
        # financial_institution=kw.get('financial_institution')
        """This route is called when adding a product to cart (no options)."""
        sale_order = request.website.sale_get_order(force_create=True)
        if sale_order.state != 'draft':
            request.session['sale_order_id'] = None
            sale_order = request.website.sale_get_order(force_create=True)

        product_custom_attribute_values = None
        if kw.get('product_custom_attribute_values'):
            product_custom_attribute_values = json.loads(kw.get('product_custom_attribute_values'))

        no_variant_attribute_values = None
        if kw.get('no_variant_attribute_values'):
            no_variant_attribute_values = json.loads(kw.get('no_variant_attribute_values'))

        sale_order._cart_update(
            product_id=int(product_id),
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values,
            product_brand_id= int(product_brand_id) or False,
            # financial_institution= financial_institution or False
        )



        if kw.get('express'):
            return request.redirect("/shop/checkout?express=1")

        return request.redirect("/shop/cart")


    def _prepare_product_values(self, product, category, search, **kwargs):
        res=super(WebsiteSale,self)._prepare_product_values( product, category, search, **kwargs)
        brands=[]
        # financial_institutions=[]
        for brand in request.env['website.product.brand'].sudo().search([]):
            brands.append({'id':brand.id,'name':brand.name})
        res['brands']=brands
        # for financial_institution in request.env['financial_institution'].sudo().search([]):
        #     financial_institutions.append({'id':financial_institution.id,'name':financial_institution.name})
        # res['financial_institutions']=financial_institutions



        return res

