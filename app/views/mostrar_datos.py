import flet as ft
from typing import Any
from app.services.transacciones_api_productos import list_products
from app.styles.estilos import Colors, Textos_estilos

def products_view(page: ft.Page) -> ft.Control:
    # 1. Obtener los productos desde Supabase
    productos_bd = list_products()
    
    # Encabezados
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    # 2. Llenar los datos recorriendo lo que nos regresó Supabase
    data = []
    
    if not productos_bd:
        # Si está vacío o hubo error
        data.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Crea la tabla 'productos' en Supabase", color="red")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
                ft.DataCell(ft.Text("-")),
            ])
        )
    else:
        # Recorremos cada producto.
        for prod in productos_bd:
            data.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(prod.get("nombre", "")))),
                        ft.DataCell(ft.Text(str(prod.get("cantidad", "")))),
                        ft.DataCell(ft.Text(str(prod.get("ingreso", "")))),
                        ft.DataCell(ft.Text(str(prod.get("min", "")))),
                        ft.DataCell(ft.Text(str(prod.get("max", "")))),
                    ]
                )
            )

    # Se crea la tabla con los datos dinámicos
    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48
    )

    return tabla
