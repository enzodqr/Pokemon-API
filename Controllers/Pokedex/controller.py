from flask_restful import Resource
from flask import request

from Models.Pokedex.model import PokedexModel
from Utils.Responses.response import HttpResponse


class PokedexController(Resource):
    @staticmethod
    def get():
        try:
            pokemons = PokedexModel.get_all()
            if pokemons:
                response = list(map(PokedexModel.map_pokemon, pokemons))
                return HttpResponse.status_200_ok(response)

            return HttpResponse.status_404_not_found('There is no content in data base')
        except Exception as ex:
            return HttpResponse.status_500_internal_server_error(ex)


class PokemonController(Resource):
    @staticmethod
    def post():
        try:
            data = request.json
            pokemon = PokedexModel(**data)
            pokemon.insert_one()
            return HttpResponse.status_201_created(pokemon.to_json)
        except Exception as ex:
            return HttpResponse.status_500_internal_server_error(ex)

    @staticmethod
    def update():
        try:
            data = request.json
            pokemon = PokedexModel(**data)
            pokemon.update_one()
            return HttpResponse.status_201_created(pokemon.to_json)
        except Exception as ex:
            return HttpResponse.status_500_internal_server_error(ex)
