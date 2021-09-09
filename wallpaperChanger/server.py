import http.server
from wallpaperChanger.server_codes import SERVER_URL
from urllib.parse import urlparse

class   RequestHandler(http.server.BaseHTTPRequestHandler):
    code  = None
    def __init__(self, request: bytes, client_address, server):
        super().__init__(request, client_address, server)

    def do_GET(self):
        # print(self.client_address)
        RequestHandler.code = self.path[self.path.find('code=') + len('code='):]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Got authorization code: {}".format(RequestHandler.code).encode())

def get_callback_code():
    host = urlparse(SERVER_URL).hostname
    port = int(urlparse(SERVER_URL).port)
    server = http.server.HTTPServer(server_address=(host, port), RequestHandlerClass=RequestHandler)
    server.handle_request()
    return RequestHandler.code