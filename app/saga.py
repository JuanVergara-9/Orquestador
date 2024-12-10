import requests
import time
from flask import current_app

class SagaOrchestrator:
    def __init__(self):
        self.catalog_service_url = current_app.config['CATALOG_SERVICE_URL']
        self.payment_service_url = current_app.config['PAYMENT_SERVICE_URL']
        self.inventory_service_url = current_app.config['INVENTORY_SERVICE_URL']
        self.purchase_service_url = current_app.config['PURCHASE_SERVICE_URL']

    def execute(self, order_data):
        try:
            self.retry(self.reserve_inventory, order_data)
            self.retry(self.process_payment, order_data)
            self.retry(self.confirm_purchase, order_data)
            self.retry(self.update_catalog, order_data)
            return {"status": "success"}
        except Exception as e:
            self.compensate(order_data)
            return {"status": "failure", "reason": str(e)}

    def reserve_inventory(self, order_data):
        response = requests.post(f'{self.inventory_service_url}/reserve', json=order_data)
        response.raise_for_status()

    def process_payment(self, order_data):
        response = requests.post(f'{self.payment_service_url}/process', json=order_data)
        response.raise_for_status()

    def confirm_purchase(self, order_data):
        response = requests.post(f'{self.purchase_service_url}/confirm', json=order_data)
        response.raise_for_status()

    def update_catalog(self, order_data):
        response = requests.post(f'{self.catalog_service_url}/update', json=order_data)
        response.raise_for_status()

    def compensate(self, order_data):
        # Logic to compensate in case of failure
        pass

    def retry(self, func, *args, retries=3, delay=2):
        for attempt in range(retries):
            try:
                return func(*args)
            except Exception as e:
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    raise e