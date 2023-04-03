from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/generate_quote", methods=["POST"])
def generate_quote():
    data = request.get_json()
    criteria = data["criteria"]

    prompt = f"Here are 1-10 ratings of how I feel for the 3 categories Happiness, Anxiety, love: {', '.join(criteria)}. "
    ratings_text = '''
    The ratings work as follows:
    1 Happiness: Very sad
    5 Happiness: Neutral
    10 Happiness: Ecstatic
    1 Anxiety: No anxiety
    5 Anxiety: Some anxiety
    10 Anxiety: Very anxious
    1 Love: Feel no love
    5 Love: Feel some love
    10 Love: Feel very loved
    '''

    prompt2 = " Write a quote to help to improve the users mood based on the score provided without using the words of the categories. Also, don't use the phrase take a deep breath."
    final_prompt = prompt + ratings_text + prompt2

    print(final_prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=final_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=1,
    )

    quote = response.choices[0].text.strip()
    return jsonify({"quote": quote})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)



