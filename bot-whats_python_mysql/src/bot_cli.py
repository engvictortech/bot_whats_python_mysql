from db import insert_message, list_messages, init_db

def main():
    print("=== BOT CLI ===")
    init_db()
    while True:
        sender = input("Digite seu nome: ")
        message = input("Digite a mensagem (ou /sair para sair): ")
        if message.lower() == "/sair":
            break
        insert_message(sender, message)
        print("Mensagem enviada!")

    print("\n=== Todas as mensagens ===")
    messages = list_messages()
    for m in messages:
        print(f"{m[0]} | {m[1]}: {m[2]} ({m[3]})")

if __name__ == "__main__":
    main()
