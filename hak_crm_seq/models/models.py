from odoo import fields, models,api,_

class CRMLeadInh(models.Model):
    _inherit = 'crm.lead'

    code = fields.Char(string='Code',Tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('crm.lead') or _('New')
        res = super(CRMLeadInh, self).create(vals)
        res.post_the_code()
        return res

    def post_the_code(self):
        self.message_post(body=_(self.name))
