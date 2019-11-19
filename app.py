#import necessários
from config import *
from routes import *

#definição de ip, porta, debug, rotas.
if __name__ == "__main__":
    app.run(debug=True, host='192.168.100.130', port=8000)
