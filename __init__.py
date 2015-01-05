# 16 Strings 


# Import Statements
from flask import (
	Flask,
	render_template
)


# App Setup
app = Flask(__name__)


# Routes


@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/news")
def news():
	return render_template("news.html")

@app.route("/links")
def links():
	return render_template("links.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=True)