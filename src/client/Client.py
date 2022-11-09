import xmlrpc.client
import asyncio


class Client:
    def __init__(self) -> None:
        self.start_client()

    def start_client(self) -> None:
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")

    def convert_csv_to_xml(self):
        print("loading ... ")
        response = self.proxy.convert_csv_to_xml()
        print(response)

    def menu(self):
        opcao: str = "a"

        while opcao != "s":
            print("\na - create xml file")
            print("s - exit\n")
            opcao = input("choose an option: ")

            match opcao:
                case "a":
                    self.convert_csv_to_xml()


cliente = Client()
cliente.menu()
