from flask import Flask
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

import sqlite3

app = Flask(__name__, instance_relative_config=True)
ma = Marshmallow(app)
conn = sqlite3.connect('data_1.db', check_same_thread=False)
conn.isolation_level = None
db = conn.cursor()
bcrypt = Bcrypt(app)


# from BusTrack.views.driver import driver
# from BusTrack.views.parent import parent
# add admin blueprint
from BusTrack.views.admin import admin
from BusTrack.repository.main import create_database
from BusTrack.views.rest_api import register_rest_api

app.register_blueprint(admin, url_prefix='/admin')

# using flask restful extension to create api instead of blueprints

'''
# add parent blueprint
app.register_blueprint(parent, url_prefix='/api/v1/parent')
# add driver blueprint
app.register_blueprint(driver, url_prefix='/api/v1/driver')

### for testing
from BusTrack.controllers.UserLoginController import userLoginController

app.register_blueprint(userLoginController, url_prefix='/app')
### for testing
'''


register_rest_api(app)
create_database()
