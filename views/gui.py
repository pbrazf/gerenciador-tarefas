import tkinter as tk
import itertools
from controllers.task import TaskManager
from config import GUI_CONFIG


# Classe para novos elementos
class Gerenciador:
    def __init__(self):
        self.controlador = TaskManager()
        self.app = tk.Tk()
        self.app.geometry(GUI_CONFIG['app_geometry'])
        self.app.title(GUI_CONFIG['app_title'])
        self.campo_entrada = None
        self.task_vars = {}  # Dicionário para armazenar as variáveis dos checkboxes
        self.opcoes_ordenacao = [
            {'sql': 'data_inserido', 'label': 'Inserção'},
            {'sql': 'feito', 'label': 'Pendente'},
            {'sql': 'feito DESC', 'label': 'Feito'},
        ]
        self.ordenacao_iter = itertools.cycle(self.opcoes_ordenacao)
        self.ordenacao_atual = next(self.ordenacao_iter)  # Inicia na primeira opção
        self.linha_ultima_tarefa = 1

        # Configura a grade para que as colunas ajustem automaticamente
        self.app.grid_columnconfigure(1, weight=1)  # Coluna 1 (título da tarefa) expande

    # Elementos ---------------------------------------------------------------------------------------------------
    def button(self, text, command, column, row, text_color = 'black', fonte = ('Arial', 8)):
        btn = tk.Button(self.app, text=text, command=command, fg=text_color, font=fonte)
        btn.grid(column=column, row=row, padx=5, pady=5)

        # Adiciona os eventos de mudança de cor ao passar o mouse
        btn.bind('<Enter>', lambda event: btn.config(fg='blue'))  # Cor azul no hover
        btn.bind('<Leave>', lambda event: btn.config(fg=text_color))  # Retorna à cor original
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

    def label(self, text, column, row, padx, pady, anchor = 'w', sticky = 'w'):
        label = tk.Label(self.app, text=text, anchor=anchor)
        label.grid(column=column, row=row, padx=padx, pady=pady, sticky=sticky)

    def entry(self, width, column, row, columnspan, padx, pady, sticky):
        entrada = tk.Entry(self.app, width=width)
        entrada.grid(column=column, row=row, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return entrada

    # Elementos gráficos -----------------------------------------------------------------------------------------------------
    def btn_new_task(self):
        '''
        Cria o campo de entrada e botão 'Adicionar' na interface gráfica
        '''
        self.campo_entrada = self.entry(width=30, column=0, row=0, columnspan=2, padx=10, pady=10, sticky='ew')
        self.button(text='Adicionar', command=self.add_task, column=2, row=0, fonte=('Arial', 8, 'bold'))

        # Associa a tecla "Enter" ao botão "Adicionar"
        self.app.bind('<Return>', lambda event: self.add_task())

    # Criar um btn para ordenar as tarefas de acordo com o desejado.
    def btn_order_tasks(self):
        '''
        Cria um button para alterar a ordenação das tarefas
        '''
        # Cria um btn para ordenar 
        self.button(text=f'Ordem → {self.ordenacao_atual['label']}', command=self.order_tasks, column=1, row=self.linha_ultima_tarefa+3, fonte=('Arial', 8, 'bold'))

        self.app.grid_rowconfigure(self.linha_ultima_tarefa+2, weight=0)
    
    def btn_delete_all_tasks(self):
        '''
        Cria um button para deletar TODAS as tasks
        '''
        # Cria um btn para ordenar 
        self.button(text=f'Limpar', command=self.delete_all_tasks, column=2, row=self.linha_ultima_tarefa+1, text_color='red', fonte=('Arial', 8, 'bold'))

    def label_informacoes(self):
        '''
        Cria um label para mostrar na tela a quantidade de tarefas concluídas e pendentes
        '''

        # Guarda a quantidade de tarefas
        num_tarefas = len(self.task_vars)
        num_concluidas = sum(self.task_vars[task_id].get() for task_id in self.task_vars)
        num_pendentes = num_tarefas - num_concluidas

        # Cria um Label com as informações
        self.label(text=f'Tarefas: {num_tarefas} | Pendentes: {num_pendentes} | Concluídas: {num_concluidas}', column=1, row=self.linha_ultima_tarefa+4, padx=5, pady=5, anchor='center', sticky='ew')

        # Permite que a última linha cresça e empurre o label para baixo
        self.app.grid_rowconfigure(self.linha_ultima_tarefa+1, weight=0)  # Linha do label fixada (anteriormente podia estar sendo expandida)
        self.app.grid_rowconfigure(self.linha_ultima_tarefa+2, weight=1)  # Linha "vazia" expansível
        self.app.grid_rowconfigure(self.linha_ultima_tarefa+4, weight=0)  # Linha do label fixada
        
    def build(self):
        '''
        Exibe as tarefas na interface gráfica
        '''
        # Limpa todos os widgets existentes na tela
        for widget in self.app.winfo_children():
            widget.destroy()

        # Redesenha o campo de entrada e botão 'Adicionar'
        self.btn_new_task()

        # Atualiza a exibição das tarefas (linhas a partir de 1)
        tasks = self.controlador.get_tasks(ordenacao=self.ordenacao_atual['sql'])
        if tasks['data']:
            for i, task in enumerate(tasks['data']):
                task_id = task[0]
                task_title = task[1].capitalize()
                task_done = task[2] == 'T'

                # Criar o checkbox, label e botão de delete para cada tarefa
                self.checklist_button(task_id, task_done, column=0, row=i+1)
                self.label(task_title, column=1, row=i+1, padx=5, pady=5)
                self.button(text='-', command=lambda t_id=task_id: self.delete_task(t_id), column=2, row=i+1)
        
            # Guarda a linha da última tarefa
            self.linha_ultima_tarefa = i+1

            # Caso tenha mais de uma task, adiciona o btn de ordenação e o btn de apagar todas as tarefas
            if len(tasks['data']) > 1:
                # Adiciona o btn de ordenar 
                self.btn_order_tasks()
                # Adiciona o btn de apagar todas as tarefas
                self.btn_delete_all_tasks()

            # Mostra o status das tarefas no final da interface
            self.label_informacoes()

        else:
            # Exibir mensagem se não houver tarefas
            tk.Label(self.app, text='Nenhuma tarefa encontrada.', fg='red').grid(column=0, row=1, columnspan=3, pady=10)

        # Faz a janela se redimensionar automaticamente
        self.app.update_idletasks()  # Atualiza o layout antes de redimensionar
        self.app.geometry('')  # Faz a janela crescer automaticamente

    def start(self):
        '''
        Inicia a interface gráfica
        '''
        self.app.mainloop()

    # Funções -----------------------------------------------------------------------------------------------------
    def update_task(self, task_id, done):
        '''
        Atualiza o estado da tarefa (concluída ou não)
        '''
        # Define o estado da tarefa como 'T' (concluída) ou 'F' (pendente)
        done_flag = 'T' if done else 'F'
        self.controlador.mark_as_done(task_id, done_flag)
        print(f'Tarefa {task_id} atualizada para {'Concluída' if done else 'Pendente'}')

        # Mostra o status das tarefas atualizado 
        self.label_informacoes()

    def add_task(self):
        '''
        Adiciona uma nova tarefa ao banco de dados
        '''
        # Obter o texto do campo de entrada
        if self.campo_entrada:
            texto = self.campo_entrada.get()
            if texto.strip():
                self.controlador.add_task(title=texto)
                print(f'Tarefa adicionada: {texto}')
                self.campo_entrada.delete(0, tk.END)
                self.build()  # Atualizar a interface com a nova tarefa

                # Retorna o foco para o campo de entrada
                self.campo_entrada.focus_set()

    def delete_task(self, task_id):
        '''
        Apaga uma tarefa do banco de dados
        '''
        # Caso clicado, apagar a tarefa
        self.controlador.delete_task(task_id=task_id)
        print(f'Tarefa {task_id} apagada com sucesso!')
        # Tira a task do dicionario local
        del self.task_vars[task_id]
        # Atualizar as tarefas na interface
        self.build()

    def delete_all_tasks(self):
        '''
        Apaga uma tarefa do banco de dados
        '''
        # Caso clicado, apagar a tarefa
        self.controlador.delete_all_tasks()
        print(f'Tarefas apagadas com sucesso!')
        # Limpa o dicionário de tasks local
        self.task_vars = {}
        # Atualizar as tarefas na interface
        self.build()

    def order_tasks(self):
        '''
        Função para ordenar as tasks.

        Possibilidades de ordenação:
            - Concluídas primeiro
            - Pendentes primeiro
            - Ordem de inserção (padrão)
        '''

        # Muda a ordenação
        self.ordenacao_atual = next(self.ordenacao_iter)
        # Estrutura a interface novamente
        self.build()
