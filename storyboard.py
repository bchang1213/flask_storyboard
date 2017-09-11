from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def initializegame():
	return render_template("index.html")

@app.route("/firstchoice", methods = ["POST"])
def firstchoice():
	food1 = request.form["choice"]
	if food1 == "Children":
		return redirect("/childrenstory")
	else:
		return redirect("/death")

@app.route("/childrenstory")
def storytwo():
	return	render_template("childrenstory.html")

@app.route("/secondchoice", methods =["POST"])
def secondchoice():
	food2 = requestion.form["choice2"]
	if food2 == "":
		return redirect("")
	else:
		return redirect("")

@app.route("/death")
def dragondeath():
	return render_template("death.html")

	
app.run(debug=True)