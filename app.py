import tkinter
from task import TaskManager 

# Classe para novos elementos
class Gerenciador:
    def __init__(self):
        self.controlador = TaskManager() 
        self.app = tkinter.Tk()
        self.app.geometry('500x300')
        self.app.title('Gerenciador de Tarefas')
        self.campo_entrada = None  

    # Método para criar botões
    def button(self, text, command, padx=10, pady=10):
        btn = tkinter.Button(self.app, text=text, command=command)
        btn.pack(padx=padx, pady=pady)
        return btn

    # Método para criar um campo de entrada e botão para adicionar tarefas
    def new_task(self):
        # Campo de entrada
        self.campo_entrada = tkinter.Entry(self.app, width=30)
        self.campo_entrada.pack(pady=10)

        # Botão para adicionar tarefa
        self.button(text='Adicionar', command=self.add_task)

    # Método para salvar uma nova tarefa
    def add_task(self):
        if self.campo_entrada:
            texto = self.campo_entrada.get()  # Pega o texto do campo de entrada
            if texto.strip():  # Verifica se o texto não está vazio
                self.controlador.add_task(title=texto)  # Salva a tarefa usando o TaskManager
                print(f'Tarefa adicionada: {texto}')
                self.campo_entrada.delete(0, tkinter.END)  # Limpa o campo de entrada

    # Método para mostrar as tarefas na interface
    def show_tasks(self):
        tasks = self.controlador.get_tasks()  # Obtém as tarefas do TaskManager
        if tasks['data'] != []:
            print('Tasks:::')
            print(tasks['data'])
            for task in tasks['data']:
                print(task)
                lbl = tkinter.Label(self.app, text=task, anchor='w')
                lbl.pack(fill='x', padx=10, pady=2)
        else:
            tkinter.Label(self.app, text='Nenhuma tarefa encontrada.', fg='red').pack(pady=10)

    # Método para iniciar a interface
    def start(self):
        self.app.mainloop()


# Define esse como o arquivo principal do projeto 
if __name__ == '__main__':
    gerenciador = Gerenciador()
    # Adiciona o campo de entrada e botão para adicionar tarefas
    gerenciador.new_task()

    # Adiciona o botão para exibir tarefas
    gerenciador.button(text='Mostrar Tarefas', command=gerenciador.show_tasks)

    # Inicia a interface gráfica
    gerenciador.start()
