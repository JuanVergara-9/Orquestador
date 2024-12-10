import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:12345678@localhost:5432/orquestador')
    CACHE_TYPE = 'simple'  # Configuración básica de caché
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    INVENTORY_SERVICE_URL = 'http://localhost:5000/inventario'
    CATALOG_SERVICE_URL = 'http://localhost:5001/catalogo'
    PURCHASE_SERVICE_URL = 'http://localhost:5002/compras'
    PAYMENT_SERVICE_URL = 'http://localhost:5003/pagos'