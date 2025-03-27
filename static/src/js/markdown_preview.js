/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, onMounted, useRef, useState } from "@odoo/owl";

/**
 * Simple Markdown converter function
 * @param {string} text - The markdown text to convert
 * @returns {string} - The HTML representation
 */
function simpleMarkdownConverter(text) {
  if (!text) return "";
  // Convert basic Markdown patterns
  let html = text;

  // Convert headers
  html = html.replace(/^# (.*$)/gm, "<h1>$1</h1>");
  html = html.replace(/^## (.*$)/gm, "<h2>$1</h2>");
  html = html.replace(/^### (.*$)/gm, "<h3>$1</h3>");

  // Convert bold and italic
  html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/\*(.*?)\*/g, "<em>$1</em>");

  // Convert links
  html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>');

  // Convert code blocks
  html = html.replace(/```([\s\S]*?)```/g, "<pre><code>$1</code></pre>");

  // Convert inline code
  html = html.replace(/`(.*?)`/g, "<code>$1</code>");

  // Convert lists
  html = html.replace(/^\* (.*$)/gm, "<ul><li>$1</li></ul>");
  html = html.replace(/^- (.*$)/gm, "<ul><li>$1</li></ul>");
  html = html.replace(/^([0-9]+)\. (.*$)/gm, "<ol><li>$2</li></ol>");

  // Convert paragraphs
  html = html.replace(/\n\n(.*?)\n\n/gs, "<p>$1</p>");

  return html;
}

class MarkdownPreview extends Component {
  setup() {
    this.state = useState({
      html: "",
    });
    this.contentRef = useRef("content");
    this.rpc = useService("rpc");

    onMounted(() => {
      this.updatePreview();
    });
  }

  async updatePreview() {
    const markdownText = this.props.record.data.content;

    if (!markdownText) {
      this.state.html = "";
      return;
    }

    try {
      // Try to use the server-side conversion first
      const result = await this.rpc("/documents/markdown_to_html", {
        markdown_text: markdownText,
      });
      this.state.html = result.html;
    } catch (e) {
      // Fall back to client-side conversion
      this.state.html = simpleMarkdownConverter(markdownText);
    }
  }
}

MarkdownPreview.template = "md_documents.MarkdownPreview";

registry.category("fields").add("markdown_preview", MarkdownPreview);

export default MarkdownPreview;
