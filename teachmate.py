import openai
from textblob import TextBlob

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

def check_bias(content):
    biased_keywords = ['always', 'never', 'only', 'must']
    flags = [word for word in biased_keywords if word in content.lower()]
    
    if flags:
        return f"Potential bias detected with keywords: {', '.join(flags)}"
    else:
        return "No bias detected."

if __name__ == "__main__":
    user_prompt = "Create a lesson plan for 5th-grade science on the topic of ecosystems."
    
    # Generate content
    generated_content = generate_content(user_prompt)
    print("Generated Content:\n", generated_content)
    
    # Refine content
    refined_content = refine_content(generated_content)
    print("Refined Content:\n", refined_content)
    
    # Check for bias
    bias_report = check_bias(refined_content)
    print("Bias Report:\n", bias_report)
