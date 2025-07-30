from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.face_shape_detector import detect_face_shape
from celebrity_data import get_celebrity_suggestion
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask backend is running. Use /detect to POST an image."

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files.get('image')
    if not image:
        return jsonify({'error': 'No image uploaded'}), 400

    filepath = "temp.jpg"
    image.save(filepath)

    face_shape, gender, age = detect_face_shape(filepath)
    celebrity, beard, comment = get_celebrity_suggestion(face_shape, gender, age)

    os.remove(filepath)

    return jsonify({
        'face_shape': face_shape,
        'gender': gender,
        'age': age,
        'celebrity': celebrity,
        'beard': beard,
        'comment': comment,
        'image_url': "https://via.placeholder.com/150"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
