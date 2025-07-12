from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
       return 'Hello Docker, welcome to DevOps world'

@app.route('/health')
def health():
    return 'Server is up and running'
