from flask import Flask, request, jsonify, make_response, redirect, url_for, abort
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras import layers
from cassandra.cluster import Cluster

cluster = Cluster()

UPLOAD_FOLDER = '/root/Docker'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

numbers = [
    {
        'id': 1,
        'title': u'number1',
        'description': u'identify this number as 1',
        'done': False
    },
    {
        'id': 2,
        'title': u'number2',
        'description': u'identify this number as 2',
        'done': False
    }
]
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/mnist/upload_image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return jsonify({'upload_file': filename})

@app.route('/numbers', methods=['GET'])
def get_numbers():
    return jsonify({'numbers': numbers})


@app.route('/numbers/<int:number_id>', methods=['GET'])
def get_number(number_id):
    number = [number for number in numbers if number['id'] == number_id]
    if len(number) == 0:
        abort(404)
    return jsonify({'number': number[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.route('/numbers/upload', methods=['POST'])
def upload_number():
    if not request.json or not 'title' in request.json:
        abort(400)
    number = {
        'id': numbers[-1]['id'] + 1,
        'title':request.json['title'],
        'description':request.json.get('description', ""),
         'done':False
    }
    numbers.append(number)
    return jsonify({'number':number}) , 201


@app.route('/numbers/<int:number_id>', methods=['DELETE'])
def delete_number(number_id):
    number = [number for number in numbers if number['id'] == number_id]
    if len(number) == 0:
        abort(404)
    numbers.remove(number[0])
    return jsonify({'result': True})


@app.route('/numbers/<int:number_id>', methods=['PUT'])
def update_number(number_id):
    number = [number for number in numbers if number['id'] == number_id]
    if len(number) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    number[0]['title'] = request.json.get('title', number[0]['title'])
    number[0]['description'] = request.json.get('title', number[0]['description'])
    number[0]['done'] = request.json.get('title', number[0]['done'])
    return jsonify({'number': number})


if __name__ == '__main__':
    app.run(debug=True)
