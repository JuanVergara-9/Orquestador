from flask import Blueprint, request, jsonify
from .services import process_order
from .extension import limiter

orchestrator_bp = Blueprint('orchestrator', __name__)

@orchestrator_bp.route('/order', methods=['POST'])
@limiter.limit("5 por minuto")  # Limita a cinco solicitudes por minuto
def order():
    order_data = request.json
    result = process_order(order_data)
    return jsonify(result)