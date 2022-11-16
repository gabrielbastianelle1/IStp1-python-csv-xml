import psycopg2
import os


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

        except (Exception, psycopg2.Error) as error:
            print("Failed to fetch data", error)

    def delete_xml_file(self, id):
        self.cursor.execute(
            f"update imported_documents set estado = false where id = {id}"
        )
        self.connection.commit()
        print("deleted")

    def list_all_xml_inserted(self):
        self.cursor.execute("select * from imported_documents;")
        files = []
        for file in self.cursor:
            if file[5] == True:
                files.append(file)
        return files

    def insert_xml_to_db(self, file_name, xml_file):
        insert_statement = f"INSERT INTO imported_documents (file_name,xml) VALUES ('{file_name}', XMLPARSE (DOCUMENT %s));"
        self.cursor.execute(insert_statement, [xml_file])
        self.connection.commit()

    def create_table_and_insert_initial_xml(self):
        print(os.listdir())

        self.cursor.execute(open("schema.sql", "r").read())

        with open("movies.xml") as xml_file:
            xml = xml_file.read()
            self.cursor.execute(
                "INSERT INTO imported_documents (file_name,xml) VALUES ('movies', XMLPARSE (DOCUMENT %s));",
                [xml],
            )
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
