import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import base64
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def process_request():
    data = request.json
    image_data = data.get('image')
    text = data.get('message')
    model = data.get('model', 'GPT4')

    # Data validation:
    if not text:
        return jsonify({'error': 'Text cannot be null'}), 400

    if not image_data:
        return jsonify({'error': 'Image cannot be null'}, 400)

    image_data = re.sub('^data:image/.+;base64,', '', image_data)
    image_data = base64.b64decode(image_data)
    try:
        Image.open(BytesIO(image_data))
    except Exception as e:
        return jsonify({'error': 'Invalid image data: {}'.format(e)}), 400

    # API CALL
    # response = requests.post('http://mm-llm-api.com/classify', json={
    #     'image': image_data,
    #     'text': text,
    #     'model': model
    # })

    # if response.status_code != 200:
    #     return jsonify({'error': 'Failed to classify image'}), 500

    # response.json()

    return jsonify({ "txtMessage": "ciao" })

@app.route('/', methods=['GET'])
def is_backend_working():
    return "Ciao"

if __name__ == '__main__':
    app.run(port=5000)
