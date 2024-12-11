import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:12345678@db/orquestador')
    CACHE_TYPE = 'simple'  # Configuración básica de caché
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    INVENTORY_SERVICE_URL = os.getenv('INVENTORY_SERVICE_URL', 'http://ms_inventario:5000/inventario')
    CATALOG_SERVICE_URL = os.getenv('CATALOG_SERVICE_URL', 'http://ms_catalogo:5001/catalogo')
    PURCHASE_SERVICE_URL = os.getenv('PURCHASE_SERVICE_URL', 'http://ms_compras:5002/compras')
    PAYMENT_SERVICE_URL = os.getenv('PAYMENT_SERVICE_URL', 'http://ms_pagos:5003/pagos')