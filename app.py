from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo"

@app.route('/helloname')
def helloname():
    name = request.args.get('name')
    return f'Hola {name}'

@app.route('/byename')
def byename():
    name = request.args.get('name')
    return f'Adios {name}'

@app.route('/sum')
def sum():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None or num2 is None:
        return 'Por favor proporciona dos numeros para sumar.'
    try:
        result = int(num1) + int(num2)
    except ValueError:
        return 'Por favor proporciona dos numeros para sumar.'
    return 'La suma es ' + str(result)

@app.route('/substract')
def substract():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 is None or num2 is None:
        return 'Por favor proporciona dos numeros para restar.'
    try:
        result = int(num1) - int(num2)
    except ValueError:
        return 'Por favor proporciona dos numeros para restar.'
    return 'La resta es ' + str(result)

@app.route('/substract')
def substract():
    """
    Subtracts two numbers provided as query parameters.

    Returns:
        str: The result of the subtraction operation.
        
    Raises:
        ValueError: If the provided inputs are not valid numbers.
    """
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return f'La resta es {num1 - num2}'
    except ValueError:
        return 'Por favor proporciona dos numeros para restar.'

if __name__ == '__main__':
    app.run(debug=True)
