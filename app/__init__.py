from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import routes, models

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://webpk_28783064:wasdfer0918@sql202.freeweb.pk/webpk_28783064_rpl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b2700f33b80883:e62dadf1@us-cdbr-east-05.cleardb.net/heroku_25a5a21d8989cd7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

db.create_all()