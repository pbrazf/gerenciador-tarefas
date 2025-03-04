from views.gui import Gerenciador 

# ---------------------------------------------------------------------------------------------------------------
# Define esse como o arquivo principal do projeto
if __name__ == '__main__':
    # Instancia o gerenciador
    gerenciador = Gerenciador()

    # Exibe as tarefas e monta interface
    gerenciador.build()    

    # Inicia a interface gráfica
    gerenciador.start()
