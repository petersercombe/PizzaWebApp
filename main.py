from flask import *
from menu import *

# Initialise the web app instance
app = Flask(__name__)
app.secret_key = "AnythingYouWant"
# orderData = {}

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/order")
def order():
    session["orderData"]["collection"] = request.args["collection"]
    session.modified = True
    return render_template("order.html", collection=session["orderData"]["collection"], menu=menu)

@app.route("/customise")
def customise():
    session["orderData"]["selection"] = request.args["selection"]
    return render_template("customise.html",
                           collection=session["orderData"]["collection"],
                           menu=menu,
                           customisations=customisations,
                           selection=session["orderData"]["selection"])


@app.route("/cart")
def cartView():
    return render_template("cart.html", orderData=session["orderData"], menu=menu) # lots to do here


@app.route("/cart", methods = ["post"])
def cartPost():
    session["orderData"][str(len(session["orderData"]))] = request.form.to_dict()
    session.modified = True
    print(session["orderData"])
    return redirect("/cart")

@app.route("/remove/<key>")
def remove(key):
    session["orderData"].pop(key)
    session.modified = True
    return redirect("/cart")


app.run(debug=True)