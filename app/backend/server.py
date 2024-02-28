import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import base64
import requests
from models.CLIP import clip_model
from models.ALIGN import align_model

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
        image = Image.open(BytesIO(image_data))
    except Exception as e:
        return jsonify({'error': 'Invalid image data: {}'.format(e)}), 400

    print("Model call")
    
    # Model call: api // local
    # label = clip_model.single_image_classification(image)
    label = align_model.single_image_classification(image)
    print("Model response")
    
    return jsonify({ "txtMessage": label })



@app.route('/', methods=['GET'])
def is_backend_working():
    return "Ciao"

if __name__ == '__main__':
    app.run(port=5000)
