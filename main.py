from flask import request, redirect, render_template, session, flash, Flask
from attempt import Attempt
from genContent import getAnswers, getQuestions
import secrets

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "yks9837xkj6d#$#"

questions = getQuestions()
answers = getAnswers()

# questions choices answers
# Q = QC[0]
# C = QC[1]   
# QCA = text[nu]
# QC = QCA[0]
# A = QCA[1]

@app.before_first_request
def set_up():
        try:
                f = open("currentProgress.txt", "r")
                fileList = []
                for line in f:
                        fileList.append(line)
                a = Attempt(fileList)
                session['attempt'] = a
                f.close()
                
        except Exception:
                num = secrets.randbelow(81)
                a = Attempt(currQ=num, points=0)
                session['attempt'] = a

                text = str(a)
                f = open("currentProgress.txt", "w")
                f.write(text)
                f.close()


@app.route("/", methods=['GET'])
def indexGet():
        a = session['attempt']
        currQ = a.currQ
        QCA = questions[currQ]
        QC = QCA[0]
        query = QC[0]
        choices = QC[1]

        return render_template("index.html", query=query, choices=choices)

@app.route("/", methods=['POST'])
def indexPost():
        # how to get multiple inputs from checkboxes
        uAnswer = request.values.getlist('uAnswer')

        att = session['attempt']
        currQ = att.currQ
        answers = getAnswers()
        ans = answers[currQ]
        # answer is a tuple where [0] is the choices, [1] is the text
        choices = ans[0]
        text = ans[1]
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