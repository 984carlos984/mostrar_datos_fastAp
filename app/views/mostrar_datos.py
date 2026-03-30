import flet as ft
from typing import Any
from app.services.transacciones_api_productos import list_products, create_product
from app.styles.estilos import Colors, Textos_estilos, Card
from app.components.popup import show_popup, show_snackbar
from app.components.error import ApiError, api_error_to_text
from app.views.nuevo_editar import formulario_nuevo_editar_producto  #Se agrega la ventana de nuevo/editar

def products_view(page: ft.Page) -> ft.Control:
    ############# Nuevo producto #############
    #Esta función se ejecuta al hacer click en "Nuevo producto"
    #lo que hace en primer lugar es abrir la ventana para captura de datos
    def inicio_nuevo_producto(_e):
        #Se crea la función para transferir al formulario de nuevo producto
        async def crear_nuevo_producto(data: dict):  #Esta función se lleva a la ventana para capturar
            try:
                #Se conecta a transacciones_api_productos.py para crear en la BD un nuevo producto
                create_product(data)
                await show_snackbar(page, "Éxito", "Producto creado.", bgcolor=Colors.SUCCESS)
                close() # <- CIERRA LA VENTANA AUTOMATICAMENTE
                actualizar_data()
            except ApiError as ex:
                await show_popup(page, "Error", api_error_to_text(ex))
            except Exception as ex:
                await show_snackbar(page, "Error", str(ex), bgcolor=Colors.DANGER)

        #Se llama a la función para abrir la ventana y poder capturar los datos,
        # regresa 3 funciones(dlg, open_ y close), se ejecuta open_()
        dlg, open_, close = formulario_nuevo_editar_producto(page, on_submit=crear_nuevo_producto, initial=None)
        open_()  #Abre la ventana
    ############# FIN nuevo producto #############
    btn_nuevo = ft.Button("Nuevo producto", icon=ft.Icons.ADD, on_click=inicio_nuevo_producto)

    rows_data: list[dict[str, Any]] = []
    total_items = 0
    total_text = ft.Text("Total de productos: (cargando...)", style=Textos_estilos.H4)

    # Encabezados
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    # Se definen las filas de la tabla
    data = []

    # Se crea la tabla (vacía inicialmente)
    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48
    )

    def actualizar_data():
        productos_bd = list_products()
        tabla.rows.clear()

        if not productos_bd:
            tabla.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text("Sin productos registrados", color=Colors.DANGER)),
                    ft.DataCell(ft.Text("-")),
                    ft.DataCell(ft.Text("-")),
                    ft.DataCell(ft.Text("-")),
                    ft.DataCell(ft.Text("-")),
                ])
            )
            total_text.value = "Total de productos: 0"
        else:
            total_text.value = f"Total de productos: {len(productos_bd)}"
            for prod in productos_bd:
                tabla.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(prod.get("nombre", prod.get("name", ""))), style=Textos_estilos.H5)),
                            ft.DataCell(ft.Text(str(prod.get("cantidad", prod.get("quantity", ""))), style=Textos_estilos.H5)),
                            ft.DataCell(ft.Text(str(prod.get("ingreso", prod.get("ingreso_date", ""))), style=Textos_estilos.H5)),
                            ft.DataCell(ft.Text(str(prod.get("min", prod.get("min_stock", ""))), style=Textos_estilos.H5)),
                            ft.DataCell(ft.Text(str(prod.get("max", prod.get("max_stock", ""))), style=Textos_estilos.H5)),
                        ]
                    )
                )
        # Solo llamamos update si ya está en página
        if tabla.page:
            tabla.update()
            total_text.update()

    # Carga inicial (sin update, la página aún no existe)
    productos_iniciales = list_products()
    if not productos_iniciales:
        tabla.rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Sin productos registrados", color=Colors.DANGER)),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
            ])
        )
        total_text.value = "Total de productos: 0"
    else:
        total_text.value = f"Total de productos: {len(productos_iniciales)}"
        for prod in productos_iniciales:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(prod.get("nombre", prod.get("name", ""))), style=Textos_estilos.H5)),
                        ft.DataCell(ft.Text(str(prod.get("cantidad", prod.get("quantity", ""))), style=Textos_estilos.H5)),
                        ft.DataCell(ft.Text(str(prod.get("ingreso", prod.get("ingreso_date", ""))), style=Textos_estilos.H5)),
                        ft.DataCell(ft.Text(str(prod.get("min", prod.get("min_stock", ""))), style=Textos_estilos.H5)),
                        ft.DataCell(ft.Text(str(prod.get("max", prod.get("max_stock", ""))), style=Textos_estilos.H5)),
                    ]
                )
            )

    contenido = ft.Column(
        #expand=True,
        spacing=30,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            btn_nuevo,
            total_text,
            ft.Container(content=tabla)
        ]
    )
    tarjeta = ft.Container(content=contenido, **Card.tarjeta)

    return tarjeta
