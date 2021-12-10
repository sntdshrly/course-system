from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import Kursus

app = Flask(__name__)
app.config["SECRET_KEY"] = "123456"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wasdfer0918@localhost/rpl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def Index():
    return "Home"

if __name__ == '__main__':
    app.run(debug=True)
