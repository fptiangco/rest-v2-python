from flask import Flask
app = Flask(__name__)

@app.route("/")
def v2():
    return "v2.a"