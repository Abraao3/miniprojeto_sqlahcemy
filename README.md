# miniprojeto_sqlahcemy
Esse projeto é formado pela super dupla: Mickeias Artaxerxes Araújo Lucena e Abraão Ferreira de Medeiros

# Atividade Prático – Flask + SQLAlchemy

**Entrega:** código no GitHub + relatório curto (README explicando execução)

---

## Objetivos de Aprendizagem

1. Criar uma aplicação Flask básica com organização mínima (`app`, `templates`, `static`).
2. Utilizar Flask + SQLAlchemy para persistência de dados.
3. Implementar cadastro e login de usuários (sem necessidade de criptografia avançada, apenas conceitos básicos).
4. Criar um cadastro de produtos com CRUD completo.
5. Consolidar boas práticas iniciais no desenvolvimento de aplicações web.

---

## Requisitos do Trabalho

### 1. Estrutura da Aplicação
- Projeto organizado em pastas (`app.py` ou `__init__.py`, `templates/`, `static/`).
- Banco de dados **SQLite** ou **MySQL** configurado via SQLAlchemy.

### 2. Cadastro e Login de Usuários
- **Cadastro:** formulário com nome, e-mail e senha.  
- **Login:** validação simples (se e-mail e senha estão corretos).  
- **Sessão:** após login, usuário permanece autenticado até logout.

### 3. Cadastro de Produtos
Criar modelo **Produto** com os campos:
- `id` (chave primária)
- `nome` (string)
- `preco` (float)
- `descricao` (texto curto)

Operações necessárias:
- Criar produto (formulário)
- Listar produtos (tabela HTML)
- Editar produto
- Excluir produto

### 4. CRUD – Operações Básicas
- Cada operação deve ser feita via rotas Flask e utilizando SQLAlchemy.
- Não é necessário aplicar relacionamentos (usuários e produtos são independentes).

### 5. Interface
- Uso de **templates Jinja2**.  
- Páginas mínimas:
  - `index.html` (home)
  - `login.html`
  - `cadastro_usuario.html`
  - `produtos.html` (listagem + links para CRUD)

