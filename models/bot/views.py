#import necessários
from . import labcinza
from app import *
import quart, requests
from quart import request, session, url_for, jsonify
from config import *
from oauth2 import *


#classe do bot
class bot(object):
    def __init__(self):
       pass   

    @labcinza.route("/<int:user_id>")
    def profile_bot(user_id):
        user = mongo.users.find_one_or_404({"_id": str(user_id)}) 
        return user     