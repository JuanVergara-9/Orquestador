class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345678@localhost/orquestador'
    CACHE_TYPE = 'simple'  # Configuración básica de caché
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CATALOG_SERVICE_URL = 'http://localhost:5000/inventario'
    PAYMENT_SERVICE_URL = 'http://localhost:5001/catalogo'
    INVENTORY_SERVICE_URL = 'http://localhost:5002/compras'
    PURCHASE_SERVICE_URL = 'http://localhost:5003/pagos'