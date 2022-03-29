import mysql.connector


class MysqlConnection:

    def create_connection(self):
        print('abriu')
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="toma",
            database="gelado"
        )
