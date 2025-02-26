import pytest
from app import create_app
from app.saga import SagaOrchestrator

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def saga_orchestrator():
    return SagaOrchestrator()

def test_order_integration_success(mocker, client, saga_orchestrator):
    mocker.patch.object(saga_orchestrator, 'reserve_inventory', return_value=None)
    mocker.patch.object(saga_orchestrator, 'process_payment', return_value=None)
    mocker.patch.object(saga_orchestrator, 'confirm_purchase', return_value=None)
    mocker.patch.object(saga_orchestrator, 'update_catalog', return_value=None)
    mocker.patch('app.routes.SagaOrchestrator', return_value=saga_orchestrator)

    response = client.post('/orchestrator/order', json={"item_id": 1, "quantity": 2})
    assert response.status_code == 200
    assert response.json == {"status": "success"}

def test_order_integration_failure(mocker, client, saga_orchestrator):
    mocker.patch.object(saga_orchestrator, 'reserve_inventory', side_effect=Exception("Inventory error"))
    mocker.patch('app.routes.SagaOrchestrator', return_value=saga_orchestrator)

    response = client.post('/orchestrator/order', json={"item_id": 1, "quantity": 2})
    assert response.status_code == 200
    assert response.json == {"status": "failure", "reason": "Inventory error"}