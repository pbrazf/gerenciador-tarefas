**Sobre o Projeto**

Este projeto é um Gerenciador de Tarefas simples, criado com o objetivo de oferecer uma interface gráfica para organizar tarefas. Ele utiliza Python com Tkinter para a interface gráfica e SQLite como banco de dados para persistência dos dados.

**Funcionalidades**

O Gerenciador de Tarefas permite:
- Adicionar Tarefas: Criar novas tarefas na lista.
- Exibir Tarefas: Listar todas as tarefas, exibindo a situação (feito ou pendente).
- Atualizar Tarefas: Marcar como concluída ou pendente.
- Deletar Tarefas: Remover tarefas da lista.

**Arquitetura do Projeto**

O projeto está dividido em três arquivos principais:

- storage.py:
  Implementa uma classe Database para manipulação do banco de dados SQLite.
  Funções CRUD:
    insert_task: Insere uma nova tarefa.
    get_task: Recupera tarefas (com filtro de situação: feita ou não).
    update_task: Atualiza campos de uma tarefa.
    delete_task: Remove uma tarefa do banco.

- task.py:
  Implementa a classe TaskManager, que abstrai a comunicação com o banco de dados para facilitar a integração com a interface gráfica.

- app.py:
  Implementa a interface gráfica utilizando Tkinter.
  Permite ao usuário interagir com as tarefas por meio de botões, checkboxes e campos de entrada.

**Como Rodar o Projeto**

Pré-requisitos
  Python 3.10+
  Nenhuma biblioteca adicional é necessária, já que o projeto utiliza somente bibliotecas padrão do Python.

**Estrutura do Banco de Dados**

  A tabela Tarefas possui os seguintes campos:
    id: Identificador único da tarefa (chave primária).
    titulo: Título da tarefa (até 100 caracteres).
    feito: Indica se a tarefa foi concluída (T) ou não (F).
    data_inserido: Data de criação da tarefa (preenchida automaticamente).

**Melhorias Futuras**

  Adicionar suporte a categorias para as tarefas.
  Permitir a edição do título das tarefas diretamente pela interface gráfica.
  Adicionar uma funcionalidade de pesquisa.
  Criar notificações para lembrar o usuário de tarefas pendentes.
