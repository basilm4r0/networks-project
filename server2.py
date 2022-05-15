import socket

port = 9000
HEADER = 1024
curpath = "/home/basilmari/Desktop/ENCS3320/project_1/" # path to root directory of server
server_address = socket.gethostbyname(socket.gethostname())
address = (server_address, port)

def readfile(path):     # reads files as binary
    file = open(curpath + path, 'rb')
    response = file.read()
    file.close()
    return response

def main():     # main body. instantiates server and handles keyboard interrupt
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(address)
        server.listen(1)
        print("Web server running on  port %s, IP address %s" % (port, server_address))
        while True:
            connection, client = server.accept()
            print("client IP address: %s\nclient port: %s" % (client[0], client[1]))
            request = connection.recv(HEADER).decode('utf-8')
            message = request.split(' ')
            method = message[0]
            filepath = message[1]
            print("Request:\t%s %s" % (method, filepath))
            ok_header = 'HTTP/1.1 200 OK\n'
            redirect_header = 'HTTP/1.1 307 Temporary Redirect\n'
            try:
                if filepath == '/go' or filepath == '/cn' or filepath == '/bzu':     # determine requested page
                    if filepath == '/go':
                        header = redirect_header
                        location = 'https://www.google.com'  # site to be redirected to
                    elif filepath == '/cn':
                        header = redirect_header
                        location = 'https://www.edition.cnn.com'  # site to be redirected to
                    elif filepath == '/bzu':
                        header = redirect_header
                        location = 'https://www.birzeit.edu'  # site to be redirected to
                    connection.send(redirect_header)
                    connection.send(f'Location : {location}\n\n'.encode('utf-8'))
                elif (filepath == '/' or filepath == '/en' or filepath == '/ar' or filepath == '/index.html' or filepath == '/main.css' or filepath
                == '/bzu.png' or filepath == '/net1.jpg' or filepath == '/networking2.jpg'):
                    if filepath == '/':
                        filepath = '/main_en.html'
                        mimetype = 'text/html'      # set content type for header
                    elif filepath == '/en':
                        filepath = '/main_en.html'
                        mimetype = 'text/html'
                    elif filepath == '/ar':
                        filepath = '/main_ar.html'
                        mimetype = 'text/html'
                    elif filepath == '/index.html':
                        filepath = '/index.html'
                        mimetype = 'text/html'
                    elif filepath == '/main.css':
                        filepath = '/main.css'
                        mimetype = 'text/css'
                    elif filepath == '/bzu.png':
                        filepath = '/bzu.png'
                        mimetype = 'image/png'
                    elif filepath == '/net1.jpg':
                        filepath = '/net1.jpg'
                        mimetype = 'image/jpg'
                    elif filepath == '/networking2.jpg':
                        filepath = '/networking2.jpg'
                        mimetype = 'image/jpg'
                    file_to_open = readfile(filepath)
                    header = ok_header     # OK status code
                    header += 'Content-Type: ' + mimetype + '\n\n'  # set header
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
        <p> The IP address of the Client is %s</p>
        <p> The port number of the Client is %s</p>
        <p> The IP address of the server is %s</p>
        <p> The port number of the server is %s</p>
      </body>
    </html>''' % (client[0], client[1], address[0], address[1])      # Page not found html page
                    mimetype = 'text/html'
                    header = 'HTTP/1.1 404 Not Found\n\n'    # page not found status code
                    header += 'Content-Type: ' + mimetype + '\n\n'  # set header
                print(header)
                response = str(header) + str(file_to_open)
                response = response.encode('utf-8')
                connection.sendall(response)
                connection.close()

            except IOError:
                connection.close()
    except KeyboardInterrupt:
        print("^C pressed, stopping web server...")
        quit()

if __name__ == '__main__':
    main()
