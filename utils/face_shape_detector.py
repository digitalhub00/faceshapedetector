from deepface import DeepFace

def detect_face_shape(image_path):
    # Analyze the image
    analysis = DeepFace.analyze(img_path=image_path, actions=['gender', 'age'], enforce_detection=False)

    gender = analysis[0]['gender']
    age = int(analysis[0]['age'])

    # Example dummy face shape detection
    face_shape = "Oval"  # You can use your existing shape logic here

    return face_shape, gender.lower(), age
