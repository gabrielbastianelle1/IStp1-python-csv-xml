import xmlrpc.client


class Client:
    def __init__(self) -> None:
        self.start_client()

    def start_client(self) -> None:
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")

    def delete_xml_file(self):
        pass

    def list_all_xml_file(self):
        files = self.proxy.list_all_xml_file()

        for file in files:
            print(f"{file[0]} : {file[1]}")

    def insert_xml_file(self):
        file_name = input("Type the file name: ")
        xml_path = input("Type the path of xml file (exemple: ./teste.xml): ")

        with open(xml_path, "r") as xml_file:
            xml = xml_file.read()

        self.proxy.insert_xml_file(file_name, xml)

    def convert_csv_to_xml(self):
        print("loading ... ")
        response = self.proxy.convert_csv_to_xml()
        print(response)

    def menu(self):
        opcao: str = "a"

        while opcao != "s":
            print("\na - create xml file")
            print("b - insert xml file")
            print("c - list all xml file")
            print("d - delete xml file")
            print("s - exit\n")
            opcao = input("choose an option: ")

            match opcao:
                case "a":
                    self.convert_csv_to_xml()
                case "b":
                    self.insert_xml_file()
                case "c":
                    self.list_all_xml_file()
                case "d":
                    self.delete_xml_file()


cliente = Client()
cliente.menu()
