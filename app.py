from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = r"C:\Users\AMD\PycharmProjects\tomato_disease\model_inception.h5"
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    # Preprocessing the image
    x = image.img_to_array(img)
    # Scaling
    x = x / 255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)

    preds = np.argmax(preds, axis=1)

    if preds == [0]:
        return "Tomato_Bacterial_spot"
    elif preds == [1]:
        return "Tomato_Early_blight"
    elif preds == [2]:
        return "Tomato_Late_blight"
    elif preds == [3]:
        return "Tomato_Leaf_Mold"
    elif preds == [4]:
        return "Tomato_Septoria_leaf_spot"
    elif preds == [5]:
        return "Tomato_Spider_mites Two-spotted_spider_mite"
    elif preds == [6]:
        return "Tomato_Target_Spot"
    elif preds == [7]:
        return "Tomato_Tomato_Yellow_Leaf_Curl_Virus"
    elif preds == [8]:
        return "Tomato_Tomato_mosaic_virus"
    elif preds == [9]:
        return "Tomato_healthy"
    
@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname('__file__')
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None

if __name__ == "__main__":
    app.run()
    
   