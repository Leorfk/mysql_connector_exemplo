from uuid import uuid4
from configuration.database_configuration import MysqlConnection
from repository.database_repository import DatabaseRepository
from repository.user_role_repository import UserRoleRepository
from repository.usuario_repository import UsuarioRepository
from random import randint
from time import sleep
connection = MysqlConnection()
db_service = DatabaseRepository(connection)
user_role_repo = UserRoleRepository(db_service)
usuario_repo = UsuarioRepository(db_service)

usuario_repo.delete_all_usuario()
db_service.commit_changes()
user_role_repo.delete_all_user_role()
db_service.commit_changes()


def abafa_v1(poll_size, batch_size):
    for c in range(poll_size):
        if not db_service.conn.is_connected():
            print('conectou novamente')
            db_service.get_connection()
        try:
            for c in range(batch_size):
                id_role = randint(1, 99999999)
                print(id_role)
                user_role_repo.insert_new_user_role((id_role, str(uuid4())))
                usuario_repo.insert_new_usuario(
                    (id_role, 'xap@xap', 'toma', id_role))
                # raise Exception('mamou')
                db_service.commit_changes()
        except Exception as ex:
            print(f'deu ruim {ex}')
            db_service.rollback()
        finally:
            db_service.close_connection()


abafa_v1(1, 1)
