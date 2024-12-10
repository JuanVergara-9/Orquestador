from flask import Blueprint, request, jsonify
from .services import process_order

orchestrator_bp = Blueprint('orchestrator', __name__)

@orchestrator_bp.route('/order', methods=['POST'])
def order():
    order_data = request.json
    result = process_order(order_data)
    return jsonify(result)