from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify(status=404, result="Invalid input format"), 404

@app.route('/add/<float:numberA>/<float:numberB>', methods=['GET'])
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify(status=200, result=result)

@app.route('/minus/<float:numberA>/<float:numberB>', methods=['GET'])
def minus(numberA, numberB):
    result = numberA - numberB
    return jsonify(status=200, result=result)

@app.route('/multiply/<float:numberA>/<float:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify(status=200, result=result)

@app.route('/divide/<float:numberA>/<float:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify(status=400, result="Division by zero error")
    result = numberA / numberB
    return jsonify(status=200, result=result)

@app.route('/')
def home():
    return jsonify(
        status=200,
        message="Calculator API is running",
        endpoints={
            "add": "/add/<number1>/<number2>",
            "subtract": "/minus/<number1>/<number2>",
            "multiply": "/multiply/<number1>/<number2>",
            "divide": "/divide/<number1>/<number2>"
        }
    )
