from repository.database_repository import DatabaseRepository
class UserRoleRepository:

    def __init__(self, database: DatabaseRepository):
        self.database = database
        self.__table = 'user_role'

    def insert_new_user_role(self, params: tuple):
        query = f'INSERT INTO {self.__table} (id_role, texto_role) VALUES (%s, %s)'
        try:
            self.database.execute_query(query, params)
        except Exception as e:
            print(f'pau ao inserir item na tabela {self.__table} \n Erro: {e}')
    
    def delete_all_user_role(self):
        self.database.delete_any(self.__table)
