####################################################################
# Objetivo do projeto: Site para troca de mensagens com Flask e Socket.io
# Data: 08/03/24
####################################################################

# Instalações
## pip install flet

# Import das bibliotecas
import flet as ft

# Função principal
def main(page):

    text = ft.Text("HashZap")

    # Criando popup e chat
    chat = ft.Column()

    def send_message_all(messages):

        # Adicionando mensagen no chat 
        text_message = ft.Text(message.value)
        chat.controls.append(text_message)

        page.update()

    page.pubsub.subscribe(send_message_all)

    def enviar_msg(event):
        page.pubsub.send_all(message.value)

        # Limpando o campo de msg
        message.value = ""

        page.update()

    message = ft.TextField(label="Digite sua mensagem", on_submit=enviar_msg)
    button_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    send_line = ft.Row([message, button_enviar])

    def entrar_chat(event):
        print("Entrar no chat")

        # Fechando o modal
        popup.open = False

        # Removendo elementos da página
        page.remove(button_iniciar)
        page.remove(text)

        # Criando chat
        page.add(chat)

        page.pubsub.send_all(f"{name_user.value} entrou no chat")

        page.add(send_line)

        # Atualizando a página
        page.update()



    title_popup = ft.Text("Bem vindo ao HashZap")
    name_user = ft.TextField(label="Escreva seu nome no chat")
    button_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=title_popup,
        content=name_user,
        actions=[button_entrar]
    )

    def open_popup(event):
        page.dialog = popup
        popup.open = True

        # Atualizando a página
        page.update()

    button_iniciar = ft.ElevatedButton("Iniciar chat", on_click=open_popup)
    
    
    page.add(text)
    page.add(button_iniciar)

# Rodando a aplicação
ft.app(target=main, view=ft.WEB_BROWSER)


