from .models import Order

def process_order_task(order_data):
    # Lógica para procesar la orden en segundo plano
    order = Order(**order_data)
    # Realiza las operaciones necesarias
    return order