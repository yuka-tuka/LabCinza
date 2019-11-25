#importações de pacotes
import quart.flask_patch
from .environment import *
from quart import Quart, render_template, session, redirect, url_for
from flask_pymongo import PyMongo
import uuid

#Quart async func
app = Quart(__name__, template_folder='templates')
app.config['SECRET_KEY'] = str(uuid.uuid4())   
app.config['MONGO_URI'] = env['website']['database']

#conexão database
pymongo = PyMongo(app)
mongo = pymongo.db


