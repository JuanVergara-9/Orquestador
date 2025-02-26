import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_order_route_success(mocker, client):
    mocker.patch('app.routes.process_order', return_value={"status": "success"})
    response = client.post('/orchestrator/order', json={"item_id": 1, "quantity": 2})
    assert response.status_code == 200
    assert response.json == {"status": "success"}

def test_order_route_failure(mocker, client):
    mocker.patch('app.routes.process_order', return_value={"status": "failure", "reason": "error"})
    response = client.post('/orchestrator/order', json={"item_id": 1, "quantity": 2})
    assert response.status_code == 200
    assert response.json == {"status": "failure", "reason": "error"}