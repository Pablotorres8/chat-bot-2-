
from flask import Flask, request, jsonify
from sympy import symbols, Eq, solve
import os

app = Flask(__name__)

# Ohm's Law Solver
def solve_ohms_law(voltage=None, current=None, resistance=None):
    if voltage is None:
        return f"Voltage = {current * resistance} V"
    elif current is None:
        return f"Current = {voltage / resistance} A"
    elif resistance is None:
        return f"Resistance = {voltage / current} Ω"
    else:
        return "Please leave one variable as None to solve."

# Endpoint for solving Ohm's Law
@app.route('/solve_ohms_law', methods=['POST'])
def solve_ohms():
    data = request.json
    voltage = data.get('voltage')
    current = data.get('current')
    resistance = data.get('resistance')
    result = solve_ohms_law(voltage, current, resistance)
    return jsonify({"result": result})

# Practice Problem Generator
import random

def generate_ohms_law_problem():
    voltage = random.randint(5, 50)  # Voltage in volts
    resistance = random.randint(1, 20)  # Resistance in ohms
    return f"What is the current in a circuit with {voltage}V and {resistance}Ω?", voltage, resistance

@app.route('/generate_problem', methods=['GET'])
def generate_problem():
    problem, voltage, resistance = generate_ohms_law_problem()
    return jsonify({"problem": problem, "voltage": voltage, "resistance": resistance})

if __name__ == '__main__':
    # Bind to 0.0.0.0 and use the PORT environment variable for Render compatibility
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
