from flask import Flask, jsonify, request


app = Flask(__name__)

devs = [
    {'name': 'Nathan Carlos',
     'lang': 'python',
     'id': 1
     },
    {'name': 'Victor Matheus',
     'lang': 'c#',
     'id': 2
     },
    {'name': 'Igor Marques',
     'lang': 'node.js',
     'id': 3
     }
]

@app.route('/devs', methods=['GET'])
def home():
    return jsonify(devs), 200

@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200

@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    # devs_per_id = [dev for dev in devs if dev['id'] == id]
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    return jsonify({'error': 'not found'}), 404

@app.route('/devs/<int:id>', methods=['PUT'])
def change_dev(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
            return jsonify(dev), 200
    return jsonify({'error': 'dev not found'}), 404

@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201
@app.route('/devs/<int:id>', methods=['DELETE'])
def delete_dev(id):
    index = id
    del devs[index]
    return jsonify({'message': 'deleted with successfuly'})

if __name__ == '__main__':
    app.run(Debug=True)
