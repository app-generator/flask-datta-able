# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   flask_migrate import Migrate
from   flask_minify  import Minify
from   sys import exit

from apps.config import config_dict
from apps import create_app, db
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import datetime,timedelta
# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)
    
if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG)             )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
    app.logger.info('ASSETS_ROOT      = ' + app_config.ASSETS_ROOT )
# Load environment variables from .env file
load_dotenv()

# Access the secret key from the environment
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = app_config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_TYPE'] = 'filesystem'
current_dir = os.getcwd()+"/session/storage/"
app.config['SESSION_FILE_DIR'] = current_dir 

# Create the session storage directory if it doesn't exist
os.makedirs(app.config['SESSION_FILE_DIR'], exist_ok=True)
app.config['SESSION_SQLALCHEMY'] = db
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
Session(app)
#########################################################################


if __name__ == "__main__":
    app.run()
