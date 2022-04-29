from flask import *
from menu import *

# Initialise the web app instance
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/order")
def order():
    collection = request.args["collection"]
    return render_template("order.html", collection=collection)

app.run(debug=True)