from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "ok"

# intentional syntax error
if True
    print("broken")
