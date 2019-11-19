#import necessários
import quart
from . import labcinza


#classe do board
class board(object):
    def __init__(self):
       pass

    #model da página inicial
    @labcinza.route("/")
    async def index():
       return "Página inicial"
		