from xmlrpc.server import SimpleXMLRPCServer

from src.handles.Handlexml import Handlexml
from src.db.Db import Db


class Server:
    def __init__(self) -> None:
        self.start_server()

    def start_server(self) -> None:
        server = SimpleXMLRPCServer(("localhost", 5000))
        server.register_function(self.convert_csv_to_xml, "convert_csv_to_xml")
        server.register_function(self.insert_xml_file, "insert_xml_file")

        print("server running on port 5000")

        self.connect_to_database()
        server.serve_forever()

    def insert_xml_file(self, file_name, xml_file):
        self.db.insert_xml_to_db(file_name, xml_file)

    def convert_csv_to_xml(self):
        handle = Handlexml()
        return "created!"

    def connect_to_database(self):
        self.db = Db()
        self.db.connection_db()
