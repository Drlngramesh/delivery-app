from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/')
def home():
    return "🚀 Delivery App Running"

@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    order = {
        "id": len(orders) + 1,
        "item": data.get("item"),
        "status": "pending"
    }
    orders.append(order)
    return jsonify(order)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = "delivered"
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
