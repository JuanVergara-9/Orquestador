import pytest
import requests
from app.saga import SagaOrchestrator

@pytest.fixture
def saga_orchestrator():
    return SagaOrchestrator()

def test_reserve_inventory_success(mocker, saga_orchestrator):
    mocker.patch('requests.post', return_value=mocker.Mock(status_code=200))
    order_data = {"item_id": 1, "quantity": 2}
    saga_orchestrator.reserve_inventory(order_data)
    requests.post.assert_called_once_with('http://ms_inventario:5000/inventario/reserve', json=order_data)

def test_reserve_inventory_failure(mocker, saga_orchestrator):
    mocker.patch('requests.post', return_value=mocker.Mock(status_code=500))
    order_data = {"item_id": 1, "quantity": 2}
    with pytest.raises(Exception):
        saga_orchestrator.reserve_inventory(order_data)
    requests.post.assert_called_once_with('http://ms_inventario:5000/inventario/reserve', json=order_data)