# app.py
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# In-memory database (a simple list of dictionaries)
transactions = [
    {'id': 1, 'description': 'Coffee', 'amount': -4.50, 'type': 'expense'},
    {'id': 2, 'description': 'Paycheck', 'amount': 2000.00, 'type': 'income'}
]
next_id = 3

# API endpoint to get all transactions
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

# API endpoint to add a new transaction
@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    global next_id
    data = request.get_json()
    
    if not data or 'description' not in data or 'amount' not in data:
        return jsonify({'error': 'Missing data'}), 400

    try:
        amount = float(data['amount'])
    except ValueError:
        return jsonify({'error': 'Invalid amount'}), 400

    transaction = {
        'id': next_id,
        'description': data['description'],
        'amount': amount,
        'type': 'income' if amount > 0 else 'expense'
    }
    transactions.append(transaction)
    next_id += 1
    return jsonify(transaction), 201

# Serve the frontend HTML file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
