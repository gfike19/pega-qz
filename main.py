from flask import request, redirect, render_template, session, flash, Flask
from tools import getShuffled
from question import Question

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    #TODO need set up for initial set up
    shuffled = getShuffled()
    session["allQ"] = shuffled
    session["counter"] = len(shuffled)
    if request.method == 'GET':
        allQ = session["allQ"]
        counter = session["counter"]
        question = allQ[counter]
        # Question class set up:
        # query is a tuple with the part being the question itself
        # the second part is a list with all the choices
        query = question.query[0]
        choices = question.query[1]
        counter -= 1
        session["counter"] = counter
        return render_template("index.html", query=query, choices=choices)
    
    # if request.method == 'POST':
    #     uAnswer = request.form['uAnswer']
    #     msg = ""

    #     if uAnswer == answers[counter[0]]
        # TODO finish post


if __name__ == "__main__":
    app.run()