from flask import Flask, request, render_template, session

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def intro():
    if request.method == "POST":
        theGame = request.form.get("game")
        thePreDate = request.form.get("pre_date")
        thePostDate = request.form.get("post_date")
        return render_template(
            "dashboard.html", game=theGame, pre_date=thePreDate, post_date=thePostDate
        )
    if request.method == "GET":
        return render_template("intro.html")
