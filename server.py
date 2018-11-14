import FolderHTTPServer
import json
from http.server import HTTPServer

PORT = 8080

Handler = FolderHTTPServer.FolderHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()