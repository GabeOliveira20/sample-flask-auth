from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Session <- conexão ativa com o banco de dados


@app.route("/Hello World", methods=["GET"])
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)    