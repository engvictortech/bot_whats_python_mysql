

# 🤖 Bot Conversacional Python + MySQL  

Aprenda, teste e explore um bot interativo que salva mensagens em banco de dados MySQL e pode ser integrado ao WhatsApp.  

---

## 📝 Funcionalidades  
- Recebe mensagens do usuário no terminal (CLI).  
- Responde de forma dinâmica com respostas pré-definidas e palavras-chave.  
- Salva todas as mensagens no banco MySQL.  
- Estrutura pronta para integração com WhatsApp via **Twilio API**.  
- Fácil de estender com novas funcionalidades.  

---

## 💻 Tecnologias  
- Python **3.13**  
- MySQL **8**  
- `mysql-connector-python`  
- `python-dotenv`  
- (Opcional) Twilio API para WhatsApp  

---

## 📂 Estrutura do Projeto  

```bash
bot_python_mysql/

│

├─ venv/                  # Ambiente virtual  

├─ src/                   # Código-fonte  

│  ├─ __init__.py         # Marca src como pacote Python  

│  ├─ db.py               # Conexão MySQL + funções CRUD  

│  ├─ bot_cli.py          # Bot no terminal  

│  └─ bot_whatsapp.py     # Bot conversacional avançado  

│

├─ docs/                  # Documentação e mídias  

│  └─ bot_demo.gif        # 🎬 GIF mostrando o bot em ação  

│

├─ .env                   # Credenciais de ambiente  

├─ .gitignore             # Ignora venv, .env e arquivos temporários  

├─ requirements.txt       # Dependências Python  

└─ README.md              # Documentação do projeto  

🚀 Como usar

1. Clone o repositório:

git clone https://github.com/engvictortech/bot_python_mysql.git
cd bot_python_mysql

2. Crie e ative o ambiente virtual:

python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

3. Instale as dependências:

pip install -r requirements.txt

4. Configure o arquivo .env:

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=botdb

5. Rode a lversão WhatsApp (Twilio)::

python src/bot_whatsapp.py


🎬 Demonstração do Bot

 ![Bot em ação](https://github.com/engvictortech/bot_python_mysql/blob/main/docs/bot_demo.gif?raw=true)


📌 Autor

👨‍💻 Projeto desenvolvido por Victor Hugo Miranda Crispim.






