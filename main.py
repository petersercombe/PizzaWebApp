from flask import *
from menu import *

# Initialise the web app instance
app = Flask(__name__)

orderData = {}

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/order")
def order():
    collection = request.args["collection"]
    return render_template("order.html", collection=collection, menu=menu)

@app.route("/customise")
def customise():
    collection = request.args["collection"]
    selection = request.args["selection"]
    return render_template("customise.html",
                           collection=collection,
                           menu=menu,
                           customisations=customisations,
                           selection=selection)


@app.route("/cart")
def cartView():
    return render_template("cart.html", orderData=orderData) # lots to do here


@app.route("/cart", methods = ["post"])
def cartPost():
    orderData[str(len(orderData))] = request.form.to_dict()
    print(orderData)
    return redirect("/cart")

@app.route("/remove/<key>")
def remove(key):
    orderData.pop(key)
    return redirect("/cart")


app.run(debug=True, host='0.0.0.0')