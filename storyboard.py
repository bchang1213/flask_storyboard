from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = '%4#(^10304@@*80e8w7'

# Load upon start
@app.route("/")
def initializegame():
	return render_template("index.html")

# form submit of the dragon's first choice
@app.route("/firstchoice", methods = ["POST"])
def firstchoice():
		return redirect("/childrenstory")

#display the dragon's second choices
@app.route("/childrenstory")
def storytwo():
	return	render_template("childrenstory.html")


# form submit of the dragon's second choice
@app.route("/secondchoice", methods =["POST"])
def secondchoice():
		return redirect("/veganstory")

@app.route("/veganstory")
def win():
	return render_template("veganstory.html")

# route of the dragon when dead
@app.route("/death", methods =["POST"])
def dragondeath():
	return render_template("death.html")


app.run(debug=True)