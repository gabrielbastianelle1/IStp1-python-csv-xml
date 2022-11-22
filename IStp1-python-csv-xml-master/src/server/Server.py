from xmlrpc.server import SimpleXMLRPCServer

from src.handles.Handlexml import Handlexml
from src.db.Db import Db
from src.handles.Handlevalidation import Handlevalidation


class Server:
    def __init__(self) -> None:
        self.start_server()

    def start_server(self) -> None:
        server = SimpleXMLRPCServer(("localhost", 5000), allow_none=True)
        server.register_function(self.convert_csv_to_xml, "convert_csv_to_xml")
        server.register_function(self.insert_xml_file, "insert_xml_file")
        server.register_function(self.list_all_xml_file, "list_all_xml_file")
        server.register_function(self.delete_xml_file, "delete_xml_file")
        server.register_function(self.query, "query")

        print("server running on port 5000")

        self.connect_to_database()
        server.serve_forever()

    def query(self, query):
        return self.db.query(query)

    def delete_xml_file(self, id) -> None:
        self.db.delete_xml_file(id)

    def list_all_xml_file(self) -> list:
        files = self.db.list_all_xml_inserted()
        return files

    def insert_xml_file(self, file_name, xml_file, xml_path) -> str:
        handlevalidation = Handlevalidation()

        if handlevalidation.validate(xml_path, "movies.xsd"):
            self.db.insert_xml_to_db(file_name, xml_file)
            return "xml inserted"
        else:
            return "xml is not valid"

    def convert_csv_to_xml(self) -> str:
        handle = Handlexml()
        return "created!"

    def connect_to_database(self) -> None:
        self.db = Db()
        self.db.connection_db()
        self.db.create_table_and_insert_initial_xml()
