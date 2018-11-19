from flask import request, redirect, render_template, session, flash, Flask
from tools import getShuffled
import secrets

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "yks9837xkj6d#$#"
shuffled = getShuffled()

# questions choices answers
# Q = QC[0]
# C = QC[1]   
# QCA = text[nu]
# QC = QCA[0]
# A = QCA[1]

@app.before_first_request
def set_up():
        try:
                f = ("currentProgress.txt", "r")
                lst = []
                for line in f:
                        lst.append(line)
                session["counter"] = 0
                QCA = shuffled[0]
                session["QCA"] = QCA
        except Exception as e:

@app.route("/", methods=['GET'])
def indexGet():
        QCA = session['QCA']
        QC = QCA[0]
        query = QC[0]
        choices = QC[1]

        f = open("currentProgress.txt", "a+")
        return render_template("index.html", query=query, choices=choices)

@app.route("/", methods=['POST'])
def indexPost():
        # how to get multiple inputs from checkboxes
        uAnswer = request.values.getlist('uAnswer')

        QCA = session['QCA']
        # answer is a tuple where [0] is the choices, [1] is the text
        choices = QCA[1][0]
        text = QCA[1][1]
        answer = "The correct answers are:"
        missed = []

        if uAnswer == choices:
                answer = "ol korrect!"
        else:
                for each in choices:
                        if each not in uAnswer:
                        missed.append(each)
                for each in missed:
                        answer += "\n"+str(each + 1)
                        answer += text

        return render_template("answer.html", answer=answer)

if __name__ == "__main__":
        app.run()