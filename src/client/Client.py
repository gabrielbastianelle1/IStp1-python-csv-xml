import xmlrpc.client
import os

from queries import queries


class Client:
    def __init__(self) -> None:
        self.start_client()

    def start_client(self) -> None:
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")

    def query(self, xml_id, query_id):
        for query in queries:
            if query["query_id"] == query_id:
                response = self.proxy.query(query["function"](xml_id))
                if (len(response)==0):
                    print("There is no data")
                    input()
                    return
                
                response.insert(0, query["head"])

                for value in response:
                    print(value)

        print("\n")

    def delete_xml_file(self) -> None:
        self.list_all_xml_file()

        id = input("insert id to delete: ")

        self.proxy.delete_xml_file(id)

    def list_all_xml_file(self) -> None:
        files = self.proxy.list_all_xml_file()

        for file in files:
            print(f"{file[0]} : {file[1]}")

    def insert_xml_file(self) -> None:
        print("THE XML YOU WANT TO INSERT SHOULD BE SAME DIRECTORY AS CLIENT")
        file_name = input("type the file name: ")
        xml_path = input("type the path of xml file (exemple: test.xml): ")

        path = os.path.dirname(os.path.abspath(__file__))
        path=path+f"/{xml_path}"

        with open(xml_path, "r") as xml_file:
            xml = xml_file.read()

        response = self.proxy.insert_xml_file(file_name, xml, path)

        print(response)

    def convert_csv_to_xml(self) -> None:

        total_lines = int(input("insert total lines to convert: "))

        print("loading ... ")
        response = self.proxy.convert_csv_to_xml(total_lines)
        print(response)

    def clean_bash(self) -> None:
        os.system("clear")

    def menu_xml(self):
        self.clean_bash()
        self.list_all_xml_file()
        xml_id = input('\nchoose xml id file: ')
        return xml_id
            

    def menu_queries(self, xml_id) -> None:
        opcao: str = "a"

        while opcao != "s":
            print("a - order country per amount of movies")
            print("b - order movie per score")
            print("c - all data movie")
            print("d - count movies pr rating")
            print("s - back")
            opcao = input("choose an option: ")
            self.clean_bash()

            match opcao:
                case "a":
                    self.query(xml_id, 1)
                case "b":
                    self.query(xml_id, 2)
                case "c":
                    self.query(xml_id, 3)
                case "d":
                    self.query(xml_id, 4)

    def menu(self) -> None:
        opcao: str = "a"

        while opcao != "s":
            print("\na - convert xml file")
            print("b - insert xml file")
            print("c - list all xml file")
            print("d - delete xml file")
            print("e - queries menu")
            print("s - exit\n")
            opcao = input("choose an option: ")
            self.clean_bash()

            match opcao:
                case "a":
                    self.convert_csv_to_xml()
                case "b":
                    self.insert_xml_file()
                case "c":
                    self.list_all_xml_file()
                case "d":
                    self.delete_xml_file()
                case "e":
                    xml_id=self.menu_xml()
                    self.menu_queries(xml_id)


cliente = Client()
cliente.menu()
