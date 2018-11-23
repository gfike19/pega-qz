from flask import request, redirect, render_template, session, flash, Flask
from attempt import Attempt
from genContent import getAnswers, getQuestions
import secrets
import os

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

# @app.before_first_request
# def set_up():
# 	f = open("currentProgress.txt", "a")


# 	# f = open("currentProgress.txt", "w+")
	

# 	a = None
# 	if os.path.getsize("currentProgress.txt") > 0:
# 		fileList = f.readlines()
# 		a = Attempt(fileList)
# 		session['attempt'] = a
# 		f.close()
# 	else:
# 		num = secrets.randbelow(81)
# 		a = Attempt(currQ=num, points=0)
# 		session['attempt'] = a
# 		text = str(a)
# 		f.write(text)
# 		f.close()
	

@app.route("/", methods=['GET'])
def indexGet():
	num = secrets.randbelow(81)
	a = Attempt(num, 0)
	currQ = num
	QC = questions[currQ]
	query = QC[0]
	choices = QC[1]

	session["attempt"] = a

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