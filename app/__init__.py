from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://webpk_28783064:wasdfer0918@sql202.freeweb.pk/webpk_28783064_rpl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b2700f33b80883:e62dadf1@us-cdbr-east-05.cleardb.net/heroku_25a5a21d8989cd7?reconnect=true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models