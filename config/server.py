#importações de pacotes
import quart.flask_patch
from quart import Quart, render_template, session, redirect, url_for
import uuid

#Quart async func
app = Quart(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())   





