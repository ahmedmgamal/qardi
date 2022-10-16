odoo.define('website_custom.website_sale', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
require('website_sale.website_sale');


publicWidget.registry.WebsiteSale.include({

        _handleAdd: function ($form) {
        var self = this;
        this.$form = $form;

        var productSelector = [
            'input[type="hidden"][name="product_id"]',
            'input[type="radio"][name="product_id"]:checked'
        ];

        var productReady = this.selectOrCreateProduct(
            $form,
            parseInt($form.find(productSelector.join(', ')).first().val(), 10),
            $form.find('.product_template_id').val(),
            false
        );

        return productReady.then(function (productId) {
            $form.find(productSelector.join(', ')).val(productId);

            self.rootProduct = {
                product_id: productId,
                quantity: parseFloat($form.find('input[name="add_qty"]').val() || 1),
                product_brand_id: parseFloat($form.find('select[name="product_brand_id"]').val() || 0),
                financial_institution: parseFloat($form.find('select[name="financial_institution"]').val() || 0),
                product_custom_attribute_values: self.getCustomVariantValues($form.find('.js_product')),
                variant_values: self.getSelectedVariantValues($form.find('.js_product')),
                no_variant_attribute_values: self.getNoVariantAttributeValues($form.find('.js_product'))
            };

            return self._onProductReady();
        });
    },

});

return publicWidget.registry.WebsiteSaleOptions;

});
