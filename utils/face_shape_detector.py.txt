import random

def detect_face_shape(image_path):
    face_shapes = ['Oval', 'Round', 'Square', 'Diamond', 'Heart']
    genders = ['male', 'female']
    age = random.randint(18, 45)

    face_shape = random.choice(face_shapes)
    gender = random.choice(genders)

    return face_shape, gender, age
