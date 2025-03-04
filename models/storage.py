import sqlite3
from config import DATABASE_CONFIG

'''
A ideia é desenvolver um CRUD completo:
    C: Criar novas tarefas
    R: Mostrar tarefas
    U: Atualizar tarefas (feito/não feito)
    D: Deletar tarefas 
'''

# Criando uma classe para manipulação do banco de dados
class Database:
    def __init__(self, db_name=DATABASE_CONFIG['db_name']):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()
    
    # Função para criar a tabela Tarefas (caso não exista)
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT(100),   
            feito CHAR DEFAULT 'F',
            data_inserido DATE DEFAULT (DATE('now'))
            )
        '''
        try:
            self.cur.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Erro ao criar a tabela: {e}')

    # Função para INSERIR uma tarefa
    def insert_task(self, titulo):
        # Monta query
        query = '''INSERT INTO Tarefas (titulo) 
        VALUES (?)'''
        try:
            self.cur.execute(query, (titulo, ))
            self.conn.commit()
            return {'status': 200, 'message': 'Tarefa adicionada com sucesso!'}
        except sqlite3.Error as e:
            return {'status': 500, 'message': f'Erro ao adicionar tarefa: {e}'}

    # Função para MOSTRAR tarefas
    def get_task(self, situacao_tarefa=('F', 'T'), ordenacao = 'data_inserido'):
        # Cria os placeholders
        placeholders = ', '.join('?' * len(situacao_tarefa))
        # Monta query
        query = f'''
        SELECT * FROM Tarefas WHERE feito IN ({placeholders}) 
        ORDER BY {ordenacao} 
        '''
        try:
            self.cur.execute(query, situacao_tarefa)
            return {'status': 200, 'data': self.cur.fetchall()}
        except sqlite3.Error as e:
            return {'status': 500, 'message': f'Erro ao adicionar tarefa: {e}'}

    # Função para ATUALIZAR tarefas (Por enquanto só vai atualizar o título e a situação da tarefa)
    def update_task(self, tarefa_id, **fields): # **fiels permite passar uma quantidade indefinida de parâmetros
        # Monta o pack de updates
        updates = ', '.join(f'{key} = ?' for key in fields)
        values = list(fields.values())
        values.append(tarefa_id) # Adiciona o id ao final da lista para ser usado no último placeholder
        # Monta query
        query = f'''
        UPDATE Tarefas SET {updates} WHERE id = ?
        '''
        try:
            self.cur.execute(query, values)
            self.conn.commit()
            return {'status': 200, 'message': 'Tarefa atualizada com sucesso!'}
        except sqlite3.Error as e:
            return {'status': 500, 'message': f'Erro ao atualizar tarefa: {e}'}

    # Função para marcar tarefa como FEITO (T) /NÃO FEITO (F) -> reutilizando a função update_task
    def mark_as_done(self, tarefa_id, feito='T'):
        return self.update_task(tarefa_id, feito=feito)

    # Função para DELETAR tarefas
    def delete_task(self, id_tarefa):
        # Monta query
        query = '''
        DELETE FROM Tarefas
        WHERE id = ?
        '''
        try:    
            self.cur.execute(query, (id_tarefa,))
            self.conn.commit()   
            return {'status': 200, 'message': 'Sucesso ao deletar tarefa!'}
        except sqlite3.Error as e:
            return {'status': 500, 'message': f'Erro ao deletar tarefa: {e}'}
    
    def delete_all_tasks(self):
        # Monta a query
        query = '''
        DELETE FROM Tarefas
        '''
        try:    
            self.cur.execute(query)
            self.conn.commit()   
            return {'status': 200, 'message': 'Sucesso ao deletar tarefa!'}
        except sqlite3.Error as e:
            return {'status': 500, 'message': f'Erro ao deletar tarefa: {e}'}

    # Função para FECHAR A CONEXÃO com o banco
    def close(self):
        self.cur.close()
        self.conn.close()

    # Função para TESTAR A CONEXÃO
    def test_connection(self):
        try:
            self.cur.execute('SELECT 1')
            return 'Conexão com o banco está funcional!'
        except sqlite3.Error as e:
            return f'Erro de conexão: {e}'
        