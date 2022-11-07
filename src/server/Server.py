from xmlrpc.server import SimpleXMLRPCServer

from src.handles.Handlexml import Handlexml


class Server:
    def __init__(self) -> None:
        self.start_server()

    def start_server(self) -> None:
        server = SimpleXMLRPCServer(("localhost", 5000))
        print("server running on port 5000")

        server.serve_forever()


server = Server()
