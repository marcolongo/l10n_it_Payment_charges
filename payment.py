from openerp import fields, models
from openerp.tools.translate import _
from openerp.osv import osv

class Payment(models.Model):
    _inherit = 'account.payment.term'

    # Add a new column to the account.payment.term model 
    
    charge = fields.Float(digits=(6, 2), help="spede d'incasso")

