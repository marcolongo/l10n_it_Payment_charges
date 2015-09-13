from openerp import fields, models
from openerp import api
from openerp.osv import osv

import logging

class order(models.Model):
     _inherit = 'sale.order'
     
     def onchange_partner_id(self, cr, uid, ids, part, context=None):
        order_line_id = False
        lista = []
        obj_sale_order_line = self.pool.get('sale.order.line')
        if not part:
            return {'value': {'partner_invoice_id': False, 'partner_shipping_id': False,  'payment_term': False, 'fiscal_position': False}}

        part = self.pool.get('res.partner').browse(cr, uid, part, context=context)
        addr = self.pool.get('res.partner').address_get(cr, uid, [part.id], ['delivery', 'invoice', 'contact'])
        pricelist = part.property_product_pricelist and part.property_product_pricelist.id or False
        invoice_part = self.pool.get('res.partner').browse(cr, uid, addr['invoice'], context=context)
        payment_term = invoice_part.property_payment_term and invoice_part.property_payment_term.id or False
        if invoice_part.property_payment_term.charge != 0:
        	payment_charge = invoice_part.property_payment_term.charge  or False
        	lista.insert(0,{'name' : 'Costi d\'incasso','price_unit' : payment_charge , 'product_uom' : 1, 'product_uom_qty' : 1,'state' : 'draft', 'type' : 'make_to_stock'})
        #	order_line_id = obj_sale_order_line.create( cr, uid,{'name' : 'Costi d\'incasso','price_unit' : payment_charge , 'order_id' : 5, 'product_uom' : 1, 'state' : 'draft', 'type' : 'make_to_stock'})
        dedicated_salesman = part.user_id and part.user_id.id or uid
        val = {
            'partner_invoice_id': addr['invoice'],
            'partner_shipping_id': addr['delivery'],
            'payment_term': payment_term,
            'user_id': dedicated_salesman,
            'order_line': lista
            #'order_line': lista
        }
        delivery_onchange = self.onchange_delivery_id(cr, uid, ids, False, part.id, addr['delivery'], False,  context=context)
        val.update(delivery_onchange['value'])
        if pricelist:
            val['pricelist_id'] = pricelist
        if not self._get_default_section_id(cr, uid, context=context) and part.section_id:
            val['section_id'] = part.section_id.id
        sale_note = self.get_salenote(cr, uid, ids, part.id, context=context)
        if sale_note: val.update({'note': sale_note})  
        return {'value': val}
