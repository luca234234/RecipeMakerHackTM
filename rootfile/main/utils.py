import openai
import os


def query_chatgpt(ingredients):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": generate_prompt(ingredients)}]
    )
    return response['choices'][0]['message']['content'].replace('\n', '<br>')


def generate_prompt(ingredients):
    return str(ingredients) + """generate a short recipe with the elements from the above list witch are food ingredients  in the next format, no indents at the start of the line:
<h1 class="recipe-name">Title</h1>
    <div class="ingredients">
        <h2  class="title">Ingredients</h2>
        <ul>
            <li class="ingredient"></li>
            <li class="ingredient"></li>
        </ul>
    </div>
    <div class="steps">
        <h2 class="title">Steps</h2>
        <ol>
            <li class="step"></li>
            <li class="step"></li>
        </ol>
    </div>"""

