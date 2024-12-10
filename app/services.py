from .saga import SagaOrchestrator

def process_order(order_data):
    orchestrator = SagaOrchestrator()
    result = orchestrator.execute(order_data)
    return result