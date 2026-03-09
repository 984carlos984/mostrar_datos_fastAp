import flet as ft
#importamos todos los estilos que vamos a ocupar en los componentes
from app.styles.estilos import Buttons,Card,Colors,Inputs,Textos_estilos
#importamos los tipos de mensajes que vamos a mostrar
from app.components.popup import show_popup, show_popup_auto_close, show_snackbar

def main(page: ft.Page):
    #Crea el texto para el título
    title = ft.Text("Mi app Flet", style=Textos_estilos.H4, text_align=ft.TextAlign.CENTER)
    #Crea el texto para el subtítulo
    subtitle = ft.Text("Sistema de estilos centralizado", style=Textos_estilos.H5)
    #Crea la caja de texto para pedir el nombre
    name = ft.TextField(label="Nombre", **Inputs.INPUT_PRIMARY)

    #Crea la funcionalidad del botón (lo que va a hacer el botón al hacer click en el)
    async def on_click(e):
        #El título de la nueva ventana
        titulo="Saludo"
        #El mensaje de la nueva ventana
        mensaje=f"Hola {name.value}" #Recupera de la caja de texto, el texto que escribió el usuario
        #Mostramos el mensaje
        #Descomenta primero el show_popup, luego show_popup_auto_close y así sucesivamente, para ver como funciona
        #await show_popup(page, titulo, mensaje, Colors.PRIMARY, Colors.WHITE)
        #show_popup_auto_close cierra en automático tras 3 segundos
        #await show_popup_auto_close(page, titulo, mensaje, Colors.PRIMARY, Colors.WHITE, 3)
        await show_snackbar(page, titulo, mensaje, Colors.PRIMARY, Colors.WHITE)

    #Crea el botón:
    btn = ft.Button("Saludar", on_click=on_click, style=Buttons.BUTTON_PRIMARY)

    #Mostramos en el programa todos los componentes
    page.add(title,subtitle,name,btn)

if __name__ == "__main__":
    ft.run(main)
