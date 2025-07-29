import cv2
import numpy as np
import math
from deepface import DeepFace

def detect_face_shape(image_path):
    # Load the image and convert it to grayscale
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return "Unknown", "Unknown", 0

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        break  # Take the first detected face

    # Dummy landmarks logic (replace with dlib/mediapipe for accuracy)
    height, width, _ = face.shape
    jaw_width = width
    forehead_width = int(width * 0.8)
    cheekbone_width = int(width * 0.9)
    face_length = height

    # Dummy face shape detection based on measurements
    if abs(jaw_width - cheekbone_width) < 15 and abs(face_length - width) > 20:
        face_shape = "Oval"
    elif jaw_width > cheekbone_width:
        face_shape = "Triangle"
    elif cheekbone_width > jaw_width:
        face_shape = "Diamond"
    elif abs(jaw_width - cheekbone_width) < 10:
        face_shape = "Round"
    else:
        face_shape = "Square"

    # 🎯 Use DeepFace to detect gender and age
    try:
        analysis = DeepFace.analyze(img_path=image_path, actions=['gender', 'age'], enforce_detection=False)
        gender = analysis[0]['gender'].lower()
        age = int(analysis[0]['age'])
    except:
        gender = "unknown"
        age = 0

    # 🔧 Step 2: Gender correction logic based on face shape
    if gender == "male" and face_shape in ["Round", "Oval"]:
        gender = "female"
    elif gender == "female" and face_shape in ["Square", "Triangle"]:
        gender = "male"

    return face_shape, gender, age
