from flask import Response
from json import dumps


class HttpResponse:
    @classmethod
    def status_200_ok(cls, data):
        response = dumps({
            'status': 'success',
            'data': {
                'Pokedex': data
            }
        })

        return Response(response, mimetype='application/json', status=200)

    @classmethod
    def status_201_created(cls, data):
        response = dumps({
            'status': 'success',
            'data': {
                'Pokemon': data
            }
        })

        return Response(response, mimetype='application/json', status=201)

    @classmethod
    def status_404_not_found(cls, fail):
        response = dumps({
            'status': 'fail',
            'message': fail
        })

        return Response(response, mimetype='application/json', status=404)

    @classmethod
    def status_500_internal_server_error(cls, err):
        response = dumps({
            'status': 'error',
            'message': err
        })

        return Response(response, mimetype='application/json', status=500)
