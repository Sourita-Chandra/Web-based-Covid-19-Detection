# covid.py

import numpy as np # type: ignore
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input

model = load_model('Trained_weights/model.h5')

class RunModel:
    def __init__(self):
        pass

    @staticmethod
    def model_predict(img_path):
        img = image.load_img(str(img_path), target_size=(128, 128)) 

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)

        classes = model.predict(img_data)

        result = int(classes[0][0])

        if result == 1:
            return "Person is affected by COVID-19."
        else:
            return "Result is Normal."
