# Bot Conversacional Python + MySQL

Um **bot conversacional em Python** que salva mensagens no banco de dados MySQL.  
Ideal para aprendizado, portfólio ou demonstração de habilidades em **Python, bancos de dados e automação**.

---

## 📝 Funcionalidades

- Recebe mensagens do usuário em terminal ou CLI
- Responde de forma dinâmica com respostas pré-definidas e palavras-chave
- Salva todas as mensagens no MySQL
- Estrutura pronta para integração com WhatsApp via Twilio
- Fácil de estender com novas funcionalidades e inteligência

---

## 💻 Tecnologias

- Python 3.13
- MySQL 8
- MySQL Connector para Python
- Dotenv para variáveis de ambiente

---

## 📂 Estrutura do Projeto

bot_python_mysql/
│

├─ venv/                       # Ambiente virtual (não enviar ao GitHub)

├─ src/

│   ├─ __init__.py             # Marca src como pacote Python

│   ├─ db.py                   # Conexão MySQL + funções CRUD

│   ├─ bot_cli.py              # Bot no terminal

│   └─ bot_whatsapp.py         # Bot conversacional avançado

├─ docs/

│   └─ bot_demo.gif            # GIF ou imagem mostrando o bot em ação

├─ .env                        # Credenciais (não enviar ao GitHub)

├─ .gitignore                  # Ignorar venv, .env e arquivos temporários

├─ requirements.txt            # Dependências Python

└─ README.md                   # Documentação do projeto


---

## ⚡ Pré-requisitos

- Python 3.13
- MySQL 8
- Conta Twilio (opcional, para WhatsApp)

---

## 🚀 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/bot_python_mysql.git
cd bot_python_mysql


## 🎬 Demonstração do Bot

Veja o bot em ação:

![Bot Demo](docs/bot_demo.gif)
