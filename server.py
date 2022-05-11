import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
from of import curdir, sep

PORT = 9000

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or '/en' or '/ar' or 'main.css':
            if self.path == '/':
                self.path = '/main_en.html'
            elif self.path == '/en':
                self.path = '/main_en.html'
            elif self.path == '/ar':
                self.path = '/main_ar.html'
            elif self.path == '/index.html':
                self.path = '/index.html'
            elif self.path == '/main.css':
                self.path = '/main.css'
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        elif self.path == '/bzu.png' or '/net1.jpg':
            if self.path == '/bzu.png':
                self.path = '/bzu.png'
            elif self.path == '/net1.jpg':
                self.path = '/net1.jpg'
            try:
                file_to_open = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(file_to_open.read())


httpd = HTTPServer(('localhost', PORT), Serv)
httpd.serve_forever()
