from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/prima', methods=['POST'])
def isprime():
    data = request.get_json()
    n = data['num']
    if n < 2:
        return jsonify({'result': 'false'})
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return jsonify({'result': 'false'})
    return jsonify({'result': 'true'})

if __name__ == '__main__':
    app.run()
