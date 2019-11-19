#importações de pacotes
from quart import Quart, render_template

#Quart async func
app = Quart(__name__)
app.config['SECRET_KEY'] = 'serial-key'    





