#import necessários
from config import *
import quart, requests, asyncio, aiohttp

endpoint = env['oauth2']['endpoint']

#classe do api
class api(object):
    def __init__(self):
       pass

    def auth(token):
        return {"Authorization": f"Bearer {token}"}

    def content():
        return {"Content-Type": "application/x-www-form-urlencoded"}    
    
    def json(code):
        json = {"client_id": env["oauth2"]['login']["client_id"],
                "client_secret":env["oauth2"]['secret'],
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": env["oauth2"]['login']["redirect_uri"],
                "scope": env["oauth2"]['login']["scope"]

                }	
        return json

    async def post(session, url, headers, code):
        async with session.post(url, data=api.json(code), headers=headers) as response:
            return await response.json()
    
    async def get(session, url, headers):
        async with session.get(url, headers=headers) as response:
                return await response.json()
 
    async def callback(code):
        async with aiohttp.ClientSession() as session:
            return await api.post(session, f'{endpoint}/oauth2/token', api.content(), code)

    async def user_info(token):
        if token is None:return None
        async with aiohttp.ClientSession() as session:
            user = await api.get(session, f'{endpoint}/users/@me', api.auth(token))
            if 'code' in user:return False
            return user


    async def user_guild(token):
        if token is None:return None
        async with aiohttp.ClientSession() as session:
            user = await api.get(session, f'{endpoint}/users/@me/guilds', api.auth(token))
            if 'code' in user:return False
            return user