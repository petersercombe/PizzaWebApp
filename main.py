from flask import *
from menu import *

# Initialise the web app instance
app = Flask(__name__)
app.secret_key = "AnythingYouWant"



@app.route("/")
@app.route("/home")
def home():
    if "orderData" not in session: session["orderData"] = {}; session["price"] = 0.00
    session.modified = True
    print(session["price"])
    return render_template("index.html")

@app.route("/order")
def order():
    if "orderData" not in session: return redirect("/")
    session["orderData"]["collection"] = request.args["collection"]
    session.modified = True
    return render_template("order.html", collection=session["orderData"]["collection"], menu=menu)

@app.route("/customise")
def customise():
    if "orderData" not in session: return redirect("/")
    session["orderData"]["selection"] = request.args["selection"]
    return render_template("customise.html",
                           collection=session["orderData"]["collection"],
                           menu=menu,
                           customisations=customisations,
                           selection=session["orderData"]["selection"])


@app.route("/cart")
def cartView():
    if "orderData" not in session: return redirect("/")
    return render_template("cart.html", orderData=session["orderData"], menu=menu) # lots to do here


@app.route("/cart", methods = ["post"])
def cartPost():
    if "orderData" not in session: return redirect("/")
    session["orderData"][str(len(session["orderData"]))] = request.form.to_dict()
    session["price"] += menu[request.form["selection"]]["price"]
    session["price"] += customisations["sizes"][request.form["size"]]
    session["price"] += customisations["crusts"][request.form["crust"]]
    session["price"] += customisations["sauces"][request.form["sauce"]]
    for key, value in request.form.to_dict().items():
        if key.startswith("extra"):
            session["price"] += customisations["extras"][request.form[key]]
    print(session["price"])
    # ToDo: Store price specifically with this pizza order so it can be subtracted from the total when removed from the cart.
    session.modified = True
    return redirect("/cart")

@app.route("/remove/<key>")
def remove(key):
    if "orderData" not in session: return redirect("/")
    session["orderData"].pop(key)
    session.modified = True
    return redirect("/cart")


app.run(debug=True)