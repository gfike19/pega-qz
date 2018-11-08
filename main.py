from flask import request, redirect, render_template, session, flash, Flask
from tools import getShuffled, createQ
from question import Question
import secrets

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "yks9837xkj6d#$#"
shuffled = getShuffled()

@app.before_first_request
def set_up():
    session["counter"] = 0
    counter = 0
    session["question"] = createQ(shuffled, counter)


@app.route("/")
def index():
    if request.method == 'GET':
        q = session["question"]
        query = q.query[0]
        choices = q.query[1]
        
        return render_template("index.html", query=query, choices=choices)

if __name__ == "__main__":
    app.run()