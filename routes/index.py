#import necessários
from config import *
from models import board

#página inicial / modulo
app.register_blueprint(board.labcinza, "/")
