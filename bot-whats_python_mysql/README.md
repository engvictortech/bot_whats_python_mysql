## 🤖 Bot Conversacional WhatsApp + Python + MySQL

Aprenda, teste e explore um bot interativo integrado ao WhatsApp que salva mensagens em banco de dados MySQL.

## 📝 Funcionalidades

💬 Recebe e envia mensagens via WhatsApp (Twilio API).

🤖 Responde dinamicamente com base em palavras-chave.

💾 Salva todas as mensagens no banco de dados MySQL.

🔧 Estrutura modular para fácil manutenção e expansão.

🖥️ Versão de testes via linha de comando (CLI) disponível.

💻 Tecnologias

🐍 Python 3.13

🗄️ MySQL 8

🔌 mysql-connector-python

🔑 python-dotenv

🌐 Flask (para webhook do WhatsApp com Twilio)

📲 Twilio API para WhatsApp

## 📂 Estrutura do Projeto

bot-whats_python_mysql/

│
├─ venv/                  # Ambiente virtual  
│
├─ src/                   # Código-fonte  
│  ├─ __init__.py         # Marca src como pacote Python  
│  ├─ db.py               # Conexão MySQL + funções CRUD  
│  ├─ bot_cli.py          # Bot no terminal (teste local)  
│  └─ bot_whatsapp.py     # Bot integrado ao WhatsApp (Twilio)  
│
├─ gif/                   # Documentação e mídias  
│  └─ bot_demo.gif        # 🎬 GIF mostrando o bot em ação  
│
├─ .env                   # Credenciais de ambiente  
├─ .gitignore             # Ignora venv, .env e arquivos temporários  
├─ requirements.txt       # Dependências Python  
└─ README.md              # Documentação do projeto  

## 🚀 Como usar

## 1️⃣ Clone o repositório:

git clone https://github.com/engvictortech/bot_whats_python_mysql.git

cd bot_whats_python_mysql

## 2️⃣ Crie e ative o ambiente virtual:

python -m venv venv
.\venv\Scripts\activate   # Windows

source venv/bin/activate  # Linux/Mac


## 3️⃣ Instale as dependências:

pip install -r requirements.txt


## 4️⃣ Configure o arquivo .env:

DB_HOST=localhost

DB_USER=seu_usuario

DB_PASSWORD=sua_senha

DB_NAME=botdb

# Twilio
TWILIO_ACCOUNT_SID=seu_account_sid

TWILIO_AUTH_TOKEN=seu_auth_token

TWILIO_WHATSAPP_NUMBER=whatsapp:+seu_numero_twilio


## 5️⃣ Rode a versão CLI (teste local):

python src/bot_cli.py


## 6️⃣ Rode a versão WhatsApp (Twilio):

python src/bot_whatsapp.py

## 🎬 Demonstração do Bot



![🎬 Bot em ação](gif/bot_demo.gif)



## 👨‍💻 Projeto desenvolvido por Victor Hugo Miranda Crispim.







