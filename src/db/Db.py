import psycopg2


class Db:
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None

    def connection_db(self) -> None:
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="kasia",
                host="localhost",
                port="5432",
                database="is",
            )

            print("database connected!")

            self.cursor = self.connection.cursor()
            """ self.cursor.execute("SELECT * FROM person")

            print("Person list:")
            for person in self.cursor:
                print(person) """

        except (Exception, psycopg2.Error) as error:
            print("Failed to fetch data", error)

        finally:
            if self.connection:
                self.cursor.close()
                self.connection.close()
