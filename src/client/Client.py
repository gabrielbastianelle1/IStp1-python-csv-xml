import xmlrpc.client
import os


class Client:
    def __init__(self) -> None:
        self.start_client()

    def start_client(self) -> None:
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")

    def teste(self):
        response = self.proxy.teste()

        for value in response:
            print(value)

    def delete_xml_file(self) -> None:
        self.list_all_xml_file()

        id = input("insert id to delete: ")

        self.proxy.delete_xml_file(id)

    def list_all_xml_file(self) -> None:
        files = self.proxy.list_all_xml_file()

        for file in files:
            print(f"{file[0]} : {file[1]}")

    def insert_xml_file(self) -> None:
        file_name = input("type the file name: ")
        xml_path = input("type the path of xml file (exemple: ./teste.xml): ")

        with open(xml_path, "r") as xml_file:
            xml = xml_file.read()

        response = self.proxy.insert_xml_file(file_name, xml, xml_path)

        print(response)

    def convert_csv_to_xml(self) -> None:
        print("loading ... ")
        response = self.proxy.convert_csv_to_xml()
        print(response)

    def clean_bash(self) -> None:
        os.system("clear")

    def menu_queries(self) -> None:
        opcao: str = "a"

        while opcao != "s":
            print("\na - teste")
            print("s - back")
            opcao = input("choose an option: ")
            self.clean_bash()

            match opcao:
                case "a":
                    self.teste()

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
                    self.menu_queries()


cliente = Client()
cliente.menu()
