
import json
from odoo import http
from odoo.http import request


class DocumentController(http.Controller):
    @http.route('/documents/<int:document_id>/preview', type='http', auth='user')
    def document_preview(self, document_id, **kwargs):
        """Render a document preview"""
        document = request.env['my.document'].browse(document_id)
        if not document.exists():
            return request.not_found()

        # Check if user has access to the document
        try:
            document.check_access_rights('read')
            document.check_access_rule('read')
        except:
            return request.not_found()

        return request.render('md_documents.document_preview_template', {
            'document': document,
        })

    @http.route('/documents/markdown_to_html', type='json', auth='user')
    def markdown_to_html(self, markdown_text):
        """Convert markdown to HTML (used for preview)"""
        if markdown_text:
            return {'html': markdown_text}
        return {'html': ''}
