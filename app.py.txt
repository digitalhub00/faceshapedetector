from flask import Flask, request, jsonify
from utils.face_shape_detector import detect_face_shape
from celebrity_data import get_celebrity_suggestion
import os

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files.get('image')
    if not image:
        return jsonify({'error': 'No image uploaded'}), 400

    filepath = "temp.jpg"
    image.save(filepath)

    face_shape, gender, age = detect_face_shape(filepath)
    celebrity, beard, comment = get_celebrity_suggestion(face_shape, gender, age)

    return jsonify({
        'face_shape': face_shape,
        'gender': gender,
        'age': age,
        'celebrity': celebrity,
        'beard': beard,
        'comment': comment,
        'image_url': "https://via.placeholder.com/150"
    })
