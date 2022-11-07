import xmlrpc.client


class Client:
    def __init__(self) -> None:
        self.start_client()

    def start_client(self) -> None:
        try:
            self.proxy = xmlrpc.client.ServerProxy("http://localhost:5000/")
            print("connected do database")
        except:
            print("deu ruim")


cliente = Client()
