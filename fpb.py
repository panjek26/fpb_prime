from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class FPB(Resource):
    def post(self):
        data = request.get_json()
        a = data['a']
        b = data['b']
        while b != 0:
            a, b = b, a % b
        result = {'fpb': a}
        return jsonify(result)

api.add_resource(FPB, '/fpb')

if __name__ == '__main__':
    app.run(debug=True)
