import openai
import os
from PIL import Image
import io


def modify_image(file):
    img = Image.open(io.BytesIO(file)).convert("RGB")  # convert to PIL Image and ensure it's RGB
    width, height = img.size
    crop_side = min(width, height)
    offsetX = (width - crop_side) // 2
    offsetY = (height - crop_side) // 2
    crop_area = (offsetX, offsetY, offsetX + crop_side, offsetY + crop_side)
    img = img.crop(crop_area)
    img = img.resize((640, 640))
    return img

def query_chatgpt(ingredients):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": generate_prompt(ingredients)}]
    )
    return response['choices'][0]['message']['content'].replace('\n', '')


def generate_prompt(ingredients):
    return str(ingredients) + """generate a short recipe with the elements from the above list witch are food ingredients  in the next format, no indents at the start of the line:
<h1 class="fw-bold post-separator">Title</h1>
    <div class="post-separator mb-1 text-start">
        <h2 class="fw-bold">Ingredients</h2>
        <ul class="fs-5 fw-semibold">
            <li></li>
            <li></li>
        </ul>
    </div>
    <div class="text-start">
        <h2 class="fw-bold">Steps</h2>
        <ol class="fs-5 fw-semibold">
            <li></li>
            <li></li>
        </ol>
    </div>"""

