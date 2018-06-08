import socketserver
import threading

class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        print(data)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Server():
    HOST = '192.168.2.125'
    PORT = 8081
    def __init__(self):
        #self.server_class = ThreadedTCPRequestHandler
        self.server = ThreadedTCPServer((self.HOST, self.PORT), ThreadedTCPRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

if __name__ == "__main__":
    s = Server()
    s
