from flask import Blueprint, request, jsonify
import torch
from PIL import Image
from rootfile.main.utils import generate_prompt
import openai
import io

main = Blueprint('main', __name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5l_food.pt')


@main.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'no image'}), 400

    file = request.files['image'].read()  # get the image file
    img = Image.open(io.BytesIO(file)).convert("RGB")  # convert to PIL Image and ensure it's RGB
    img = img.resize((640, 640))
    results = model(img)
    ingredients = results.pandas().xyxy[0].value_counts('name').index.tolist()
    openai.Completion.create(
        model="",
        prompt=generate_prompt(ingredients),
        temperature=0.6,
    )
    return jsonify(ingredients)

