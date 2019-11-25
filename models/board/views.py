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
       user = await api.user_info(session.get("token", None))
       if user is False:return redirect("/logout")
       return await quart.render_template("index.html", user=user)

    #model da página callback (autenticar)
    @labcinza.route('callback')
    async def callback():
       try:
           res = await api.callback(quart.request.args.get('code'))
           session["token"] = res["access_token"]
           return redirect("/")
       except KeyError:
           return redirect("/")

    #model da página login (gerar o link)
    @labcinza.route('login')
    async def login():
      if session.get("token") is None:
         return redirect(env['oauth2']['link']+urllib.parse.urlencode(env['oauth2']['login']))
      else:
        return redirect('/')    

    #model da página perfil (perfil do usuário)
    @labcinza.route('perfil')
    async def profile():
       user = await api.user_info(session.get("token", None))
       if user is False or user is None:return redirect("/logout")
       return jsonify(user)

    #model da página guilds (listagem das guilds do usuário)
    @labcinza.route('guild')
    async def guild():
       guild = await api.user_info(session.get("token", None))
       if guild is False or guild is None:return redirect("/logout")
       return jsonify(user_guild)
    

    #model da página logout (apagar o token da session)
    @labcinza.route('logout')
    async def logout():
      if session.get("token") is None:
         return redirect("/")
      del session["token"]
      return redirect("/")      
