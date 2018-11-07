from flask import request, redirect, render_template, session, flash, Flask
from tools import getShuffled
from question import Question

app = Flask(__name__)
app.config['DEBUG'] = True
shuffled = getShuffled()
session["allQ"] = shuffled
session["counter"] = len(shuffled)
@app.route("/")
def index():

    if request.method == 'GET':
        allQ = session["allQ"]
        counter = session["counter"]
        question = allQ[counter]
        q = question.query[0]
        choices = question.query[:len(q)]
        counter -= 1
        session["counter"] = counter
        return render_template("index.html", q=q, a=choices)
    
    # if request.method == 'POST':
    #     uAnswer = request.form['uAnswer']
    #     msg = ""

    #     if uAnswer == answers[counter[0]]
        # TODO finish post


if __name__ == "__main__":
    app.run()