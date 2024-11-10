import os
from flask import Flask
from .routes import lama_api
# from app.model.initiate_db import initiate_db
# from app.model import db
# from app.mongo_model.initiate_mongo import init_mongo
from flask_cors import CORS

application = Flask(__name__, instance_relative_config=True)
app: Flask = application
CORS(app)

if 'FLASK_ENV' not in os.environ or os.environ['FLASK_ENV'].lower() == 'staging':
    app.config.from_object('app.config.Config')
elif os.environ['FLASK_ENV'].lower() == 'production':
    app.config.from_object('app.config.ProductionConfig.ProductionConfig')

app.register_blueprint(lama_api)
# initiate_db(app)
# init_mongo(app)