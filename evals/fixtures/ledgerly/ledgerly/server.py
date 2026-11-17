# ABOUTME: Tiny HTTP server for the ledgerly web UI.
# ABOUTME: Serves invoice PDFs from the invoices directory.
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

INVOICE_DIR = os.path.join(os.path.dirname(__file__), "..", "invoices")


def read_invoice(name):
    with open(os.path.join(INVOICE_DIR, name), "rb") as f:
        return f.read()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path != "/download":
            self.send_error(404)
            return
        name = parse_qs(url.query).get("name", [""])[0]
        body = read_invoice(name)
        self.send_response(200)
        self.send_header("Content-Type", "application/pdf")
        self.end_headers()
        self.wfile.write(body)
