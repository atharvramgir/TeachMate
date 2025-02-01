from flask import Flask, render_template, request
import openai
from textblob import TextBlob

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'api_key'

def generate_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def refine_content(content):
    blob = TextBlob(content)
    refined_content = str(blob.correct())
    
    return refined_content

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_content = ""
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        generated_content = generate_content(user_prompt)
        refined_content = refine_content(generated_content)
        return render_template('index.html', generated_content=refined_content)
    return render_template('index.html', generated_content=generated_content)

if __name__ == '__main__':
    app.run(debug=True)
