from flask import *
from menu import *

# Initialise the web app instance
app = Flask(__name__)
app.secret_key = "AnythingYouWant"


@app.route("/")
@app.route("/home")
def home():
    if "orderData" not in session: session["orderData"] = {}
    session.modified = True
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
    return render_template("cart.html", orderData=session["orderData"], menu=menu)


@app.route("/cart", methods = ["post"])
def cartPost():
    if "orderData" not in session: return redirect("/")
    item = str(len(session["orderData"])) # Houston, we have a problem here.
    session["orderData"][item] = request.form.to_dict()
    itemPrice = menu[request.form["selection"]]["price"]
    itemPrice += customisations["sizes"][request.form["size"]]
    itemPrice += customisations["crusts"][request.form["crust"]]
    itemPrice += customisations["sauces"][request.form["sauce"]]
    for key, value in request.form.to_dict().items():
        if key.startswith("extra"):
            itemPrice += customisations["extras"][request.form[key]]
    session["orderData"][item]["itemPrice"] = itemPrice
    print (session["orderData"])

    session.modified = True
    return redirect("/cart")

@app.route("/remove/<key>")
def remove(key):
    if "orderData" not in session: return redirect("/")
    session["orderData"].pop(key)
    session.modified = True
    return redirect("/cart")


app.run(debug=True)