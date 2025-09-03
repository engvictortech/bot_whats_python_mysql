print("Conversa iniciada!")

from db import insert_message  # Salvar mensagens no MySQL
from random import choice

# from random import choice

BOT_NAME = "Alexa"  # Nome do seu bot

# Lista de respostas genéricas com o nome do bot incluído
responses = [
    f"Interessante! Me conte mais, disse {BOT_NAME}.",
    f"Uau, isso é legal! - {BOT_NAME}",
    f"Pode me explicar melhor? {BOT_NAME} quer entender.",
    f"Humm, entendi. {BOT_NAME} está prestando atenção!",
    f"Muito bom! Continue. {BOT_NAME} está curioso.",
    f"Nossa, nunca tinha pensado nisso! {BOT_NAME} se surpreendeu.",
    f"Sério? Conte mais sobre isso. {BOT_NAME} quer saber.",
    f"Que interessante! Continue falando. {BOT_NAME} está ouvindo.",
    f"Hmm... interessante ponto de vista. {BOT_NAME} concorda.",
    f"Isso é fascinante! {BOT_NAME} quer aprender mais.",
    f"Continue, {BOT_NAME} está gostando da conversa!",
    f"Não sabia disso! {BOT_NAME} está impressionado.",
]

# Função para gerar respostas mais inteligentes com palavras-chave
def generate_response(user_msg):
    msg = user_msg.lower()
    if "sim" in msg:
        return f"Que bom! Continue falando... {BOT_NAME}"
    elif "não" in msg:
        return f"Tudo bem, podemos mudar de assunto. {BOT_NAME}"
    elif "porque" in msg:
        return f"Boa pergunta! O que você acha sobre isso? {BOT_NAME}"
    elif "como" in msg:
        return f"Isso é algo que precisamos pensar juntos! {BOT_NAME}"
    elif "quando" in msg:
        return f"Não tenho certeza, mas podemos explorar juntos. {BOT_NAME}"
    elif "você" in msg:
        return f"Ah, você quer saber sobre mim? Eu sou {BOT_NAME}!"
    else:
        return choice(responses)

# Loop principal do bot
def bot_loop():
    print("=== BOT Conversacional ===")
    name = input("Oi! Qual é o seu nome? ")
    print(f"Olá {name}, vamos conversar! (digite /sair para encerrar)")

    while True:
        user_msg = input(f"{name}: ")
        if user_msg.lower() == "/sair":
            print("Até logo! 😊")
            break

        # Gera a resposta do bot
        bot_response = generate_response(user_msg)
        print(f"Bot: {bot_response}")

        # Salva mensagens no banco
        insert_message(name, user_msg)
        insert_message("Bot", bot_response)

# Executa o bot
if __name__ == "__main__":
    bot_loop()
