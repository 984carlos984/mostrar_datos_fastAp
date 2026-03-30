import sys
import os

# Añadir el directorio raíz para permitir importaciones locales
sys.path.append(os.getcwd())

from app.services.supabase_client import supabase

def inject_data():
    if not supabase:
        print("❌ Error: Supabase no está configurado correctamente en el archivo .env.")
        return

    # Datos de ejemplo
    productos_ejemplo = [
        {"nombre": "Laptop Pro 16", "cantidad": 15, "ingreso": "2024-03-25", "min": 5, "max": 20},
        {"nombre": "Monitor 4K 27\"", "cantidad": 22, "ingreso": "2024-03-26", "min": 10, "max": 30},
        {"nombre": "Teclado Mecánico RGB", "cantidad": 45, "ingreso": "2024-03-27", "min": 20, "max": 80},
        {"nombre": "Mouse Gamer Inalámbrico", "cantidad": 38, "ingreso": "2024-03-28", "min": 15, "max": 60},
        {"nombre": "Auriculares Cancelación Ruido", "cantidad": 12, "ingreso": "2024-03-29", "min": 5, "max": 15},
    ]

    print("🚀 Intentando inyectar datos en la tabla 'productos'...")

    try:
        # Intentar insertar
        response = supabase.table("productos").insert(productos_ejemplo).execute()
        
        if response.data:
            print(f"✅ ¡Éxito! Se insertaron {len(response.data)} productos.")
            for i, p in enumerate(response.data):
                print(f"   {i+1}. {p['nombre']} (Cantidad: {p['cantidad']})")
        else:
            print("⚠️ La operación terminó pero no se devolvieron datos. Verifica si la tabla existe.")

    except Exception as e:
        print(f"❌ Error al inyectar datos: {e}")
        print("\n💡 Tip: Asegúrate de que la tabla se llame 'productos' y tenga las columnas (nombre, cantidad, ingreso, min, max).")

if __name__ == "__main__":
    inject_data()
