from flask import Flask, request

app = Flask(__name__)

@app.route('/usuarios/api/v1/saludo', methods=['GET'])
def saludo_usuario():
    usuario_id = request.args.get('id')
    if usuario_id:
        return f"Hola, el id del usuario es {usuario_id}!", 200
    else:
        return "Lista de todos los usuarios.", 200
if __name__ == '__main__':
    app.run(debug=True)