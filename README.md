**Sobre o Projeto**

Este projeto é um Gerenciador de Tarefas simples, criado com o objetivo de oferecer uma interface gráfica para organizar tarefas. Ele utiliza Python com Tkinter para a interface gráfica e SQLite como banco de dados para persistência dos dados.

**Funcionalidades**

O Gerenciador de Tarefas permite:
- Adicionar Tarefas: Criar novas tarefas na lista.
- Exibir Tarefas: Listar todas as tarefas, exibindo a situação (feito ou pendente).
- Atualizar Tarefas: Marcar como concluída ou pendente.
- Deletar Tarefas: Remover tarefas da lista.

**Arquitetura do Projeto**

gerenciador_tarefas/
├── app.py         # Ponto de entrada
├── config.py      # Configurações gerais
├── models/
│   └── storage.py # Manipulação do banco de dados
├── controllers/
│   └── task.py    # Lógica de negócios
├── views/
│   └── gui.py     # Interface gráfica

Estrutura: 
- app.py: Arquivo principal que inicializa a aplicação.
- config.py: Centraliza as configurações do projeto, como informações do banco de dados e ajustes da interface gráfica.
- models/storage.py: Responsável pela manipulação direta do banco de dados SQLite.
- controllers/task.py: Contém a lógica de negócios e faz a ponte entre a interface gráfica e o banco de dados.
- views/gui.py: Gerencia os elementos visuais e interações com o usuário.

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
