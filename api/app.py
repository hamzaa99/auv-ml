from flask import Flask

app = Flask(__name__)

@app.route('/')
def super_endpoint():
    return 'Hello World'