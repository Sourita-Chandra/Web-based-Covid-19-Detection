#app.py

from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from covid import RunModel  
import os

app = Flask(__name__)

# Ensure the 'uploads' folder exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        # Save file to 'uploads' folder
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)  

        # Predict using the model
        result = RunModel.model_predict(file_path)
        
        return jsonify({'result' : result})  # Return result as JSON

    return jsonify(result="No file uploaded."), 400

if __name__ == '__main__':
    app.run(debug=True)
