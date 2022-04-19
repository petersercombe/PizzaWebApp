from flask import *

# Initialise the web app instance
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Hello, World!"


app.run()