from http.server import BaseHTTPRequestHandler
from datetime import datetime
import urllib.parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    parsed = urllib.parse.urlparse(self.path)
    letter_id = urllib.parse.parse_qs(parsed.query)["id"][0]
    self.wfile.write(letter_id.encode())
    return
