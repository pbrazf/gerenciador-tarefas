import tkinter as tk
from task import TaskManager

# Classe para novos elementos
class Gerenciador:
    def __init__(self):
        self.controlador = TaskManager()
        self.app = tk.Tk()
        self.app.geometry('350x300')
        self.app.title('Gerenciador de Tarefas')
        self.campo_entrada = None
        self.task_vars = {}  # Dicionário para armazenar as variáveis dos checkboxes

        # Configura a grade para que as colunas ajustem automaticamente
        self.app.grid_columnconfigure(1, weight=1)  # Coluna 1 (título da tarefa) expande

    # Elementos ---------------------------------------------------------------------------------------------------
    def button(self, text, command, column, row):
        btn = tk.Button(self.app, text=text, command=command)
        btn.grid(column=column, row=row, padx=5, pady=5)
        return btn

    def checklist_button(self, task_id, done, column, row):
        # Criar uma variável para armazenar o estado do checkbox
        checklist_var = tk.BooleanVar(value=done)
        self.task_vars[task_id] = checklist_var  # Salvar a variável no dicionário

        # Criar o checkbox e associar o callback
        check_btn = tk.Checkbutton(
            self.app,
            variable=checklist_var,
            command=lambda: self.update_task(task_id, checklist_var.get())
        )
        check_btn.grid(column=column, row=row, padx=5, pady=5, sticky='w')
        return check_btn
    
    def label(self, text, column, row, padx, pady):
        label = tk.Label(self.app, text=text, anchor='w')
        label.grid(column=column, row=row, padx=padx, pady=pady, sticky='w')

    def entry(self, width, column, row, columnspan, padx, pady, sticky):
        entrada = tk.Entry(self.app, width=width)
        entrada.grid(column=column, row=row, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)

    # Funções -----------------------------------------------------------------------------------------------------
    def new_task(self):
        '''
        Cria o campo de entrada e botão "Adicionar" na interface gráfica
        '''
        self.campo_entrada = self.entry(width=30, column=0, row=0, columnspan=2, padx=10, pady=10, sticky='ew')
        self.button(text='Adicionar', command=self.add_task, column=2, row=0)

    
    def show_tasks(self):
        '''
        Exibe as tarefas na interface gráfica
        '''
        # Limpa todos os widgets existentes na tela
        for widget in self.app.winfo_children():
            widget.destroy()

        # Redesenha o campo de entrada e botão "Adicionar"
        self.new_task()

        # Atualiza a exibição das tarefas (linhas a partir de 1)
        tasks = self.controlador.get_tasks()
        if tasks['data']:
            for i, task in enumerate(tasks['data']):
                task_id = task[0]
                task_title = task[1]
                task_done = task[2] == 'T'

                # Criar o checkbox, label e botão de delete para cada tarefa
                self.checklist_button(task_id, task_done, column=0, row=i+1)
                self.label(self.app, text=task_title, column=1, row=i+1, padx=5, pady=5)
                self.button(text='-', command=lambda task_id=task_id: self.delete_task(task_id), column=2, row=i+1)
        else:
            # Exibir mensagem se não houver tarefas
            tk.Label(self.app, text='Nenhuma tarefa encontrada.', fg='red').grid(column=0, row=1, columnspan=3, pady=10)

    def update_task(self, task_id, done):
        '''
        Atualiza o estado da tarefa (concluída ou não)
        '''
        # Define o estado da tarefa como 'T' (concluída) ou 'F' (pendente)
        done_flag = 'T' if done else 'F'
        self.controlador.mark_as_done(task_id, done_flag)
        print(f"Tarefa {task_id} atualizada para {'Concluída' if done else 'Pendente'}")

    def add_task(self):
        '''
        Adiciona uma nova tarefa ao banco de dados
        '''
        # Obter o texto do campo de entrada
        if self.campo_entrada:
            texto = self.campo_entrada.get()
            if texto.strip():
                task_id = self.controlador.add_task(title=texto)
                print(f'Tarefa adicionada: {texto}')
                self.campo_entrada.delete(0, tk.END)
                self.show_tasks()  # Atualizar a interface com a nova tarefa

    def delete_task(self, task_id):
        '''
        Apaga uma tarefa do banco de dados
        '''
        # Caso clicado, apagar a tarefa
        self.controlador.delete_task(task_id=task_id)
        print(f'Tarefa {task_id} apagada com sucesso!')
        # Atualizar as tarefas na interface
        self.show_tasks()

    def start(self):
        '''
        Inicia a interface gráfica
        '''
        self.app.mainloop()


# ---------------------------------------------------------------------------------------------------------------
# Define esse como o arquivo principal do projeto
if __name__ == '__main__':
    # Instancia o gerenciador
    gerenciador = Gerenciador()

    # Exibe o campo de entrada e botão "Adicionar"
    gerenciador.new_task()

    # Exibe as tarefas
    gerenciador.show_tasks()

    # Inicia a interface gráfica
    gerenciador.start()
