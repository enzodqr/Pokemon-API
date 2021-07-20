from flask import Flask
from flask_restful import Api

from Controllers.Pokedex.controller import PokedexController, PokemonController


app = Flask(__name__)
api = Api(app)

api.add_resource(PokedexController, '/pokedex')
api.add_resource(PokemonController, '/pokedex/pokemon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_debugger=False, use_reloader=False)
