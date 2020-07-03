from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def home():
#     return 

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

