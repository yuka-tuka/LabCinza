#importações de pacotes
from config import *

#filtrar o avatar
@app.template_filter('avatar')
def avatar(user):
    if user.get('avatar'):
       return "https://cdn.discordapp.com/avatars/"+user['id']+'/'+user['avatar']+'.png'
    else:
      return f"{env['website']['index']}/static/img/noimg.png"
     
#filtrar o nome do usuário
@app.template_filter('username')
def username(user):
    if user.get('username'):
     if len(user.get('username')) != 0:
        return user.get('username')
     else:
       return "Não definido"





