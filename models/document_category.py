
from odoo import api, fields, models, _


class DocumentCategory(models.Model):
    _name = 'my.document.category'
    _description = 'Document Category'
    _order = 'sequence, name'

    name = fields.Char('Category Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=10)
    parent_id = fields.Many2one('my.document.category', string='Parent Category', ondelete='cascade')
    child_ids = fields.One2many('my.document.category', 'parent_id', string='Child Categories')
    document_count = fields.Integer('# Documents', compute='_compute_document_count')
    active = fields.Boolean(default=True)
    color = fields.Integer('Color Index')
    description = fields.Text('Description')

    @api.depends('child_ids.document_count')
    def _compute_document_count(self):
        for category in self:
            domain = [('category_id', '=', category.id)]
            category.document_count = self.env['my.document'].search_count(domain)
