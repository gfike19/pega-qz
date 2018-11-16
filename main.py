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
    session["counter"] = 0
    QCA = shuffled[0]
    session["QCA"] = QCA

@app.route("/", methods=['GET'])
def indexGet():
        QCA = session['QCA']
        QC = QCA[0]
        query = QC[0]
        choices = QC[1]

        return render_template("index.html", query=query, choices=choices, answerText=answerText)

@app.route("/", methods=['POST'])
def indexPost():
        # how to get multiple inputs from checkboxes
        uAnswer = request.values.getlist('uAnswer')

        QCA = session['QCA']

        counter = session['counter'] + 1
        session['counter'] = counter
        QCA = shuffled[counter]
        QC = QCA[0]
        query = QC[0]
        choices = QC[1]
        session['QCA'] = QCA
        answerText = QCA[1]
        # answerText = ""
        # if uAnswer == lst:
        #         answerText = "Correct!"
        # else:
        #         answerText = "Incorrect " + " " + answer[len(answer) - 1]
        
        # counter = session['counter']
        # counter += 1
        # session['counter'] = counter        

        # return render_template("index.html", answerText=answerText)
        return render_template("index.html", answerText=answerText, query=query, choices=choices)

if __name__ == "__main__":
    app.run()