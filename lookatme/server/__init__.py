"""
Threaded Socket server
"""

import socket
import threading
import socketserver

class Viewer(socketserver.BaseRequestHandler):
   def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
        
class Server(object):
    def __init__(self, port):
        self.host = "localhost"
        self.port = port
        self.server = ThreadedServer((self.host, self.port), Viewer)
        
    def serve(self):
        ip, port = self.server.server_address
        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.daemon = True
        server_thread.start()


    def close(self):
        server.shutdown()
        server.server_close()
