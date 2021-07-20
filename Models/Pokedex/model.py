from DB.db import DataBase

COLLECTION = 'Pokedex'
CLIENT = DataBase(COLLECTION)


class PokedexModel:
    def __init__(self, name='', types=None, _id=''):
        if types is None:
            types = list()
        self._id = _id
        self.name = name
        self.types = types

    @classmethod
    def get_all(cls):
        try:
            return CLIENT.find()

        except Exception as err:
            return err

    @classmethod
    def get_one(cls, _id):
        try:
            pokemon = CLIENT.find_one({
                "_id": _id
            })
            return cls(**pokemon)
        except Exception as err:
            return err

    def insert_one(self):
        try:
            CLIENT.insert_one({
                '_id': self._id,
                'name': self.name,
                'types': self.types,
            })
        except Exception as err:
            return err

    def update_one(self):
        try:
            CLIENT.update_one({
                '_id': self._id
            }, {
                'name': self.name,
                'types': self.types,
            })
        except Exception as err:
            return err

    @property
    def to_json(self):
        pokemon = {
            '_id': self._id,
            'name': self.name,
            'types': self.types
        }

        return pokemon

    @staticmethod
    def map_pokemon(pokemon):
        return PokedexModel(**pokemon).to_json
