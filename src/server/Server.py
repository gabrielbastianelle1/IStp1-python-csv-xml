from xmlrpc.server import SimpleXMLRPCServer

from src.handles.Handlexml import Handlexml


class Server:
    def __init__(self) -> None:
        self.start_server()

    def start_server(self) -> None:
        server = SimpleXMLRPCServer(("localhost", 5000))
        server.register_function(self.convert_csv_to_xml, "convert_csv_to_xml")

        print("server running on port 5000")

        server.serve_forever()

    def convert_csv_to_xml(self):
        handle = Handlexml()
        return "created!"
