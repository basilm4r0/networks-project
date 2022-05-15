import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler

port = 9000
curpath = "/home/basilmari/Desktop/ENCS3320/project_1/" # path to root directory of server

class Serv(BaseHTTPRequestHandler):     # define request handler
    def do_GET(self):       # define response method
        try:
            if self.path == '/go' or self.path == '/cn' or self.path == '/bzu':     # determine requested page
                if self.path == '/go':
                    self.send_response(307)     # redirection status code
                    self.send_header('Location', 'https://www.google.com')  # site to be redirected to
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
            == '/bzu.png' or self.path == '/net1.jpg' or self.path == '/networking2.jpg'):
                if self.path == '/':
                    self.path = '/main_en.html'
                    mimetype = 'text/html'      # set content type for header
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
                elif self.path == '/networking2.jpg':
                    self.path = '/networking2.jpg'
                    mimetype = 'image/jpg'
                file_to_open = readfile(self.path)
                self.send_response(200)     # OK status code
                self.send_header('Content-type', mimetype)  # set header
                self.end_headers()
                self.wfile.write(file_to_open)  # respond with requested page
            else:           # page not found
                file_to_open = '''<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title> Error </title>
  </head>
  <body>
    <h1> HTTP/1.1 404 Not Found </h1>
    <h2 style="color:red;"> The file is not found </h2>
    <div>
      <b> Ahmad Abu Masood - 1192647</b> <br/>
      <b> Basil Mari - 1191027</b> <br/>
      <b> Mohammad Nafee - 1173027</b>
    </div>
    <p> The IP number of the Client is %s</p>
    <p> The port number of the Client is %s</p>
  </body>
</html>''' % (self.address_string(), port)      # Page not found html page
                mimetype = 'text/html'
                self.send_response(404)     # page not found status code
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(file_to_open.encode('utf-8'))      # respond with page not found page

        except IOError:
            self.send_error(404, "File not found %s" % self.path)

def readfile(path):     # reads files as binary
    file = open(curpath + path, 'rb')
    response = file.read()
    file.close()
    return response

def main():     # main body. instantiates server and handles keyboard interrupt
    try:
        server = HTTPServer(('', port), Serv)
        print("Web server running on  port %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C pressed, stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    main()
