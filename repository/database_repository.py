from configuration.database_configuration import MysqlConnection
class DatabaseRepository:

    def __init__(self, db_connection: MysqlConnection):
        self.db_connection = db_connection
        self.conn = self.db_connection.create_connection()

    def execute_query(self, query: str, params: tuple):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        cursor.close()
    
    def delete_any(self, table):
        query = f'delete from {table}'
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()
        

    def commit_changes(self):
        self.conn.commit()
    
    def get_connection(self):
        return self.db_connection.create_connection()