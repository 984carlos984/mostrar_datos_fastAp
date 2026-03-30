# app/services/transacciones_api_productos.py
from app.services.supabase_client import supabase

# Obtiene la lista de productos de Supabase
def list_products(limit: int = 20, offset: int = 0):
    if not supabase:
        return []
    try:
        # Se asume que la tabla se llama "productos"
        response = supabase.table("productos").select("*").range(offset, offset + limit - 1).execute()
        return response.data
    except Exception as e:
        print(f"Error al listar productos: {e}")
        return []

# Obtiene un producto por ID
def get_product(product_id: str):
    if not supabase:
        return {}
    try:
        response = supabase.table("productos").select("*").eq("id", product_id).single().execute()
        return response.data
    except Exception as e:
        print(f"Error al obtener producto {product_id}: {e}")
        return {}

# Crea un producto nuevo
def create_product(data: dict):
    if not supabase:
        return {}
    try:
        response = supabase.table("productos").insert(data).execute()
        if response.data:
            return response.data[0]
        return {}
    except Exception as e:
        print(f"Error al crear producto: {e}")
        return {}

# Actualiza un producto
def update_product(product_id: str, data: dict):
    if not supabase:
        return {}
    try:
        response = supabase.table("productos").update(data).eq("id", product_id).execute()
        if response.data:
            return response.data[0]
        return {}
    except Exception as e:
        print(f"Error al actualizar producto {product_id}: {e}")
        return {}

# Borra un producto
def delete_product(product_id: str):
    if not supabase:
        return {}
    try:
        response = supabase.table("productos").delete().eq("id", product_id).execute()
        return response.data
    except Exception as e:
        print(f"Error al borrar producto {product_id}: {e}")
        return {}
