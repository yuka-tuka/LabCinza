#import necessários
from config import *
from models import board, bot

#rota home
app.register_blueprint(board.labcinza, "/")
#rotas do bot
app.register_blueprint(bot.labcinza, "/bot")