from flask import request, redirect, render_template, session, flash, Flask
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

@app.route("/", methods=['GET'])
def indexGet():

	try:
		allQ = list(session["allQ"])
	except:
		allQ = []
	
	try:
		scoreText = str(session["score"]) + "/81"
	except:
		scoreText = ""
		
	num = secrets.randbelow(81)

	while num in allQ:
		num = secrets.randbelow(81)
	
	allQ.append(num)
	
	QC = questions[num]
	query = QC[0]
	choices = QC[1]

	session["currQ"] = num
	session["allQ"] = allQ

	return render_template("index.html", query=query, choices=choices, scoreText=scoreText)

@app.route("/", methods=['POST'])
def indexPost():
	# how to get multiple inputs from checkboxes
	uAnswer = request.values.getlist('uAnswer')
	currQ = session["currQ"]
	ans = answers[currQ]
	# answer is a tuple where [0] is the choices, [1] is the text
	choices = ans[0]
	text = ans[1]
	answer = "The correct answers are:"
	missed = []
	
	try:
		score = session["score"]
	except:
		score = 0

	if uAnswer == choices:
		answer = "ol korrect!"
		score += 1
		session["score"] = score
	else:
		for each in choices:
				if each not in uAnswer:
						missed.append(each)
		for each in missed:
				answer += "\n"+str(int(each) + 1)
		answer += "\n" + text
		answer += "\nFor " + str(questions[currQ])

	scoreText = str(score) + "/81"
	session["score"] = score

	return render_template("answer.html", answer=answer, scoreText=scoreText)

if __name__ == "__main__":
	app.run()