from flask import Flask, request, render_template
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config.from_object('config.Config')

openai.api_key = app.config['OPENAI_API_KEY']

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