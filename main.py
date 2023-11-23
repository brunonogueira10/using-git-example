from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello , my name is Bruno, and this is a example about Git</p>"