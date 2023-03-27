from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Prima(Resource):
    def post(self):
        data = request.get_json()
        num = data['num']
        if num > 1:
            for i in range(2,(num//2)):
                if (num % i) == 0:
                    result = {'is_prima': False}
                    return jsonify(result)
            else:
                result = {'is_prima': True}
                return jsonify(result)
        else:
            result = {'is_prima': False}
            return jsonify(result)
        
api.add_resource(Prima, '/prima')

if __name__ == '__main__':
    app.run(debug=True)
