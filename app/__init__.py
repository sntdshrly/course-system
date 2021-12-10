from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wasdfer0918@localhost/rpl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from app import routes, models