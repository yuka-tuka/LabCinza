#importações de pacotes
import json

#carregar os dados da dashboard
with open('./data/json/data.json', encoding='utf-8') as env:
    env = json.load(env)


