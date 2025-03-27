
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Document(models.Model):
    _name = 'my.document'
    _description = 'Markdown Document'
    _order = 'sequence, id desc'

    name = fields.Char('Document Title', required=True)
    code = fields.Char('Document Number', readonly=True, copy=False, default='/')
    sequence = fields.Integer('Sequence', default=10)
    category_id = fields.Many2one('my.document.category', string='Category', 
                                  required=True)
    author_id = fields.Many2one('res.users', string='Author', required=True, 
                                default=lambda self: self.env.user)
    content = fields.Html('Content', help="Document content in Markdown format")
    content_html = fields.Html('Content (HTML)', compute='_compute_content_html', store=True,
                              sanitize=True, sanitize_tags=True, sanitize_attributes=True)
    version = fields.Integer('Version', default=1)
    active = fields.Boolean(default=True)
    date_created = fields.Datetime('Created on', default=fields.Datetime.now, readonly=True)
    date_updated = fields.Datetime('Last Updated on', default=fields.Datetime.now, 
                                   readonly=True)
    tags = fields.Many2many('my.document.tag', string='Tags')
    
    @api.depends('content')
    def _compute_content_html(self):
        """Convert content to HTML for preview"""
        for document in self:
            if document.content:
                # Simply use the HTML content directly for preview
                document.content_html = document.content
            else:
                document.content_html = False
    
    @api.model_create_multi
    def create(self, vals_list):
        """Override create to set date_created and document number"""
        for vals in vals_list:
            if vals.get('code', '/') == '/':
                vals['code'] = self.env['ir.sequence'].next_by_code('my.document') or 'ch-0000'
        records = super(Document, self).create(vals_list)
        return records
    
    def write(self, vals):
        """Override write to update date_updated and version"""
        if 'content' in vals or 'name' in vals:
            vals['date_updated'] = fields.Datetime.now()
            vals['version'] = self.version + 1
        
        return super(Document, self).write(vals)
    
    def copy(self, default=None):
        """Override copy to add '(copy)' to name"""
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        
        return super(Document, self).copy(default)
    
    def toggle_active(self):
        """Override toggle_active to archive/unarchive documents"""
        return super(Document, self).toggle_active()


class DocumentTag(models.Model):
    _name = 'my.document.tag'
    _description = 'Document Tag'
    
    name = fields.Char('Tag Name', required=True)
    color = fields.Integer('Color Index')
