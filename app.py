from flask import Flask, request, render_template, jsonify
from transformers import AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch
import io

app = Flask(__name__)

# Load the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model_path = "model"  # Directory where the model is stored
model = AutoModelForImageClassification.from_pretrained(model_path)
model = model.to(device)
model.eval()

# Load the image processor
image_processor = AutoImageProcessor.from_pretrained(model_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file provided'}), 400

    # Preprocess the image
    image = Image.open(io.BytesIO(file.read())).convert('RGB')
    inputs = image_processor(images=image, return_tensors="pt").to(device)

    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1).cpu().numpy().flatten()

    # Define the class labels
    labels = [
        "Benign keratosis-like lesions",
        "Basal cell carcinoma",
        "Actinic keratoses",
        "Vascular lesions",
        "Melanocytic nevi",
        "Melanoma",
        "Dermatofibroma"
    ]

    # Combine labels and probabilities
    results = {label: float(prob) for label, prob in zip(labels, probabilities)}

    return jsonify(results)

@app.route('/predict_image')
def predict_image():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
