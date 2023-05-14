from flask import Blueprint, request, jsonify, render_template, g, make_response
import torch
from PIL import Image
from rootfile.main.utils import query_chatgpt


import io

main = Blueprint('main', __name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5l_food.pt')


@main.route('/')
def home():
    return render_template('Home.html')


@main.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'no image'}), 400

    file = request.files['image'].read()  # get the image file
    img = Image.open(io.BytesIO(file)).convert("RGB")  # convert to PIL Image and ensure it's RGB
    img = img.resize((640, 640))
    results = model(img)
    ingredients = results.pandas().xyxy[0].value_counts('name').index.tolist()
    recipe_html = query_chatgpt(ingredients)
    return recipe_html


@main.route('/recipe')
def recipe():
    return render_template('Recpies.html')
