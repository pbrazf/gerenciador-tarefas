from models.storage import Database
from config import GENERAL_CONFIG

# Classe para manipulação das tarefas
class TaskManager:
    def __init__(self):
        self.db = Database()

    def add_task(self, title):
        if len(title) > GENERAL_CONFIG['max_task_title_length']:
            return {'status': 400, 'message': 'Título muito longo!'}
        return self.db.insert_task(title)

    def get_tasks(self, status=('F', 'T')):
        return self.db.get_task(status)

    def update_task(self, task_id, **fields):
        return self.db.update_task(task_id, **fields)

    def mark_as_done(self, task_id, done='T'):
        return self.db.update_task(task_id, feito=done)

    def delete_task(self, task_id):
        return self.db.delete_task(task_id)

    def close_connection(self):
        self.db.close()
