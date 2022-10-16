
import datetime

from odoo import http
from odoo import fields
from odoo.exceptions import AccessError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class OdooAcademy(http.Controller):

    @http.route('/academy/offers/', auth='public', website=True)
    def display_subjects(self, sortby=None, **kw):
        commercial_partner = request.env.user.name

        courses = http.request.env['sale_order_offer'].search([('partner_id.name','=',commercial_partner)])
        return http.request.render('website_custom.portal_openacademy_courses', {
            'courses': courses,
            'page_name': 'course',
        })

    @http.route('/academy/<model("sale_order_offer"):course>/', auth='public', website=True)
    def display_course_detail(self, course):
        print(course.order_id.name)
        order=request.env['sale.order'].search([('name','=',course.order_id.name)])
        print(order)
        order.write({
            'offer':course.name.id
        })

        return http.request.render('website_custom.portal_openacademy_courses1', {'course': course, 'page_name': 'course'})
        # get from query string if not on json param




class AcademyCustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self,counter):
        values = super(AcademyCustomerPortal, self)._prepare_home_portal_values(counter)
        count_courses = http.request.env['sale_order_offer'].search_count([])
        values.update({
            'count_courses': count_courses,
        })
        return values
