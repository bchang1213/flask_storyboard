from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def initializegame():
	return render_template("index.html")

@app.route("/firstchoice", methods = ["POST"])
	food1 = request.form["choice"]
	if food1 == "Children":
		return redirect("/childrenstory")
	else:
		return redirect("/death")
app.run(debug=True)