from flask import request, redirect, render_template, session, flash, Flask
from genContent import *
import random

app = Flask(__name__)
app.config['DEBUG'] = True 

answers = getAnswers()
questions = getQuestions()
order = []

for num in range(0,len(answers)):
    order.append(num)

random.shuffle(order)
counter = 0

@app.route("/")
def index():

    if request.method == 'GET':
        temp = questions.items()[counter]
        q = temp[0]
        a = temp[1]
        return render_template("index.html", q=q, a=a)
    
    if request.method == 'POST':
        uAnswer = request.form['uAnswer']
        msg = ""

        if uAnswer == answers[counter[0]]
        # TODO finish post


if __name__ == "__main__":
    app.run()