from views.gui import Gerenciador 

# ---------------------------------------------------------------------------------------------------------------
# Define esse como o arquivo principal do projeto
if __name__ == '__main__':
    # Instancia o gerenciador
    gerenciador = Gerenciador()

    # Exibe o campo de entrada e botão 'Adicionar'
    gerenciador.new_task()

    # Exibe as tarefas
    gerenciador.show_tasks()

    # Inicia a interface gráfica
    gerenciador.start()
