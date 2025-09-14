from flask import Flask, request, render_template
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables in a file called .env
load_dotenv(override=True)

# Get the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
openai = OpenAI()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    response = openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-4o",
    )
    answer = response.choices[0].message.content
    return render_template('index.html', answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
