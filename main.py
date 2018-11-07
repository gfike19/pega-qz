from flask import request, redirect, render_template, session, flash, Flask
from tools import getShuffled, createQ
from question import Question
import secrets

app = Flask(__name__)
app.config['DEBUG'] = True
shuffled = getShuffled()

@app.before_first_request
def set_up():
    session["counter"] = 0
    session["question"] = createQ


@app.route("/")
def index():
    if request.method == 'GET':
        

        
       


if __name__ == "__main__":
    app.run()