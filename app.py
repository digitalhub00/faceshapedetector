from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.face_shape_detector import detect_face_shape
from celebrity_data import get_celebrity_suggestion
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Home route to test if backend is running
@app.route('/')
def home():
    return "Flask backend is running. Use /detect to POST an image."

# Main detection route
@app.route('/detect', methods=['POST'])
def detect():
    image = request.files.get('image')
    if not image:
        return jsonify({'error': 'No image uploaded'}), 400

    # Save the uploaded image temporarily
    filepath = "temp.jpg"
    image.save(filepath)

    # Run face shape detection and get suggestions
    face_shape, gender, age = detect_face_shape(filepath)
    celebrity, beard, comment = get_celebrity_suggestion(face_shape, gender, age)

    # Delete the temporary image to clean up
    os.remove(filepath)

    # Return results as JSON
    return jsonify({
        'face_shape': face_shape,
        'gender': gender,
        'age': age,
        'celebrity': celebrity,
        'beard': beard,
        'comment': comment,
        'image_url': "https://via.placeholder.com/150"  # You can replace this later
    })

# Start the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0
