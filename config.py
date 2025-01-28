# config.py

# Configurações do banco de dados
DATABASE_CONFIG = {
    'db_name': 'banco.db',  # Nome do arquivo do banco de dados
}

# Configurações da interface gráfica
GUI_CONFIG = {
    'app_title': 'Gerenciador de Tarefas',  # Título da janela
    'app_geometry': '350x300',             # Tamanho inicial da janela
    'padding': {
        'x': 10,  # Padding horizontal
        'y': 10   # Padding vertical
    }
}

# Configurações gerais
GENERAL_CONFIG = {
    'max_task_title_length': 100,  # Comprimento máximo do título da tarefa
}
