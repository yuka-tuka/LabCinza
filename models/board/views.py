#import necessários
from . import labcinza
from app import *
import quart, requests
from quart import request, session, url_for, jsonify
from config import *
from oauth2 import *


#classe do board
class board(object):
    def __init__(self):
       pass

    #model da página inicial
    @labcinza.route("/")
    async def index():
        return "Páginas [Login, Callback, Perfil, Guild, Logout]"
    
    #model da página callback (autenticar)
    @labcinza.route('callback')
    async def callback():
        code = quart.request.args.get('code')
        try:
            res = await api.callback(code)
        except requests.exceptions.HTTPError:
            return "Invalid Code, try again."
        session["token"] = res["access_token"]
        return redirect('/')

    #model da página login (gerar o link)
    @labcinza.route('login')
    async def login():
      if session.get("token") is None:
         return redirect(config['oauth2']['link']+urllib.parse.urlencode(config['oauth2']['login']))
      else:
        return redirect('/')
    
    #model da página perfil (perfil do usuário)
    @labcinza.route('perfil')
    async def profile():
      if session.get("token") is None:
         return redirect("/")
      try:
        user = await api.user_info(session.get("token"))
      except requests.exceptions.HTTPError:
         return "Token não é válido, ou expirou!"
      return jsonify(user)

    #model da página guilds (listagem das guilds do usuário)
    @labcinza.route('guild')
    async def guild():
      if session.get("token") is None:
         return redirect("/")
      try:
        guild = await api.user_guild(session.get("token"))
      except requests.exceptions.HTTPError:
         return "Token não é válido, ou expirou!"
      return jsonify(guild)
    
    #model da página logout (apagar o token da session)
    @labcinza.route('logout')
    async def logout():
      if session.get("token") is None:
         return redirect("/")
      del session["token"]
      return redirect("/")      