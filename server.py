import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler

port = 9000
curpath = "/home/basilmari/Desktop/ENCS3320/project_1/"

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/go' or self.path == '/cn' or self.path == '/bzu':
                if self.path == '/go':
                    self.send_response(307)
                    self.send_header('Location', 'https://www.google.com')
                    self.end_headers()
                elif self.path == '/cn':
                    self.send_response(307)
                    self.send_header('Location', 'https://www.edition.cnn.com')
                    self.end_headers()
                elif self.path == '/bzu':
                    self.send_response(307)
                    self.send_header('Location', 'https://www.birzeit.edu')
                    self.end_headers()
                self.wfile.write('\n'.encode('utf-8'))
            if (self.path == '/' or self.path == '/en' or self.path == '/ar' or self.path == '/index.html' or self.path == '/main.css' or self.path
            == '/bzu.png' or self.path == '/net1.jpg'):
                if self.path == '/':
                    self.path = '/main_en.html'
                    mimetype = 'text/html'
                elif self.path == '/en':
                    self.path = '/main_en.html'
                    mimetype = 'text/html'
                elif self.path == '/ar':
                    self.path = '/main_ar.html'
                    mimetype = 'text/html'
                elif self.path == '/index.html':
                    self.path = '/index.html'
                    mimetype = 'text/html'
                elif self.path == '/main.css':
                    self.path = '/main.css'
                    mimetype = 'text/css'
                elif self.path == '/bzu.png':
                    self.path = '/bzu.png'
                    mimetype = 'image/png'
                elif self.path == '/net1.jpg':
                    self.path = '/net1.jpg'
                    mimetype = 'image/jpg'
                file_to_open = readfile(self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(file_to_open)
            else:
                self.path = 'wrong.html'
                mimetype = 'text/html'
                file_to_open = readfile(self.path)
                self.send_response(404)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(file_to_open)

        except IOError:
            self.send_error(404, "File not found %s" % self.path)

def readfile(path):
    file = open(curpath + path, 'rb')
    response = file.read()
    file.close()
    return response

def main():
    try:
        server = HTTPServer(('', port), Serv)
        print("Web server running on  port %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C pressed, stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    main()
