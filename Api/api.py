from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='¡Hola, esta es tu API!')

@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return jsonify(message=f'¡Hola, {nombre}!')

if __name__ == '__main__':
    app.run(debug=True)

# comando en terminal para ejecutar api.py:   python Api/api.py
 