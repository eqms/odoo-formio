# Copyright 2018 Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

from odoo import api, fields, models, _


class VersionAsset(models.Model):
    _name = 'formio.version.asset'
    _description = 'Formio Version Asset'
    _order = 'sequence ASC'

    version_id = fields.Many2one('formio.version', string='Version')
    type = fields.Selection([('js', 'js'), ('css', 'css')], string='Type')
    attachment_id = fields.Many2one('ir.attachment', string="Attachment", required=True, ondelete='cascade')
    attachment_type = fields.Selection(related='attachment_id.type', string='Attachment Type', readonly=True)
    sequence = fields.Integer(string='Sequence', default=1)
    url = fields.Char(compute='_compute_url')

    @api.depends('attachment_id')
    def _compute_url(self):
        for r in self:
            if r.attachment_type == 'url':
                r.url = r.attachment_id.url
            elif r.attachment_type == 'binary':
                r.url = '/web/content/{attachment_id}'.format(attachment_id=r.attachment_id.id)
