import os as __os

from flask import Flask

# initialize app
app = Flask(__name__)

# app configuration setup

# read default base configuration
app.config.from_object('config.base')

# override by environment specific configuration files
__env_attrs = __os.environ
env = __env_attrs.get('ENV')

if not env:
    raise Exception("set {ENV} environment variable to start application")
elif env == "dev":
    import config.dev
    app.config.from_object(config.dev)
elif env == "qa":
    import config.qa
    app.config.from_object(config.qa)
elif env == "staging":
    import config.stage
    app.config.from_object(config.stage)
elif env == "prod":
    import config.prod
    app.config.from_object(config.prod)
elif env == "local":
    import config.local
    app.config.from_object(config.local)

# override by external environment configuration file
app.config.from_envvar('APP_SETTINGS', silent=True)

# configure database
from connectors.mysql.mysql_connector import db
db.init_app(app)

# create tables
from dbmodels.user import User
db.create_all(app=app)

# register blueprints
from api.url_register import bp as url_register_bp
app.register_blueprint(url_register_bp)

# run server
if env == "local":
    app.run("localhost", 5000, debug=app.config.get("DEBUG"))
