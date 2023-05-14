import openai
import os


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

