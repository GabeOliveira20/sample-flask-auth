from flask import Flask, jsonify, request
from database import db
from flask_login import LoginManager, login_user
from models.user import User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # Inicializa extensões
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Callback para carregar usuário
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Rota de login
    @app.route('/login', methods=["POST"])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and password: 
            #Login
            user = User.query.filter_by(username=username).first()

            if user and password == password:
                return jsonify({"message": "Autenticação realizada com sucesso"}), 200

        return jsonify({"message": "Credenciais inválidas"}), 400

    # Rota simples de teste
    @app.route("/hello", methods=["GET"])
    def hello_world():
        return "Hello, World!"

    return app

# Executa a aplicação
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Cria tabelas no banco
    app.run(debug=True)