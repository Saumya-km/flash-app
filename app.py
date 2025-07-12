# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_word():
#        return 'Hello Docker, welcome to DevOps world'

# @app.route('/health')
# def health():
#     return 'Server is up and running'
from flask import Flask, render_template, request

app = Flask(__name__)

flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
]

@app.route('/')
def index():
    card_id = int(request.args.get("card", 0))
    card = flashcards[card_id % len(flashcards)]
    return render_template("index.html", card=card, card_id=card_id)

if __name__ == "__main__":
    app.run(debug=True)

