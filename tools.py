from genContent import getAnswers, getQuestions
from question import Question
import secrets

def getShuffled():
    answers = getAnswers()
    questions = getQuestions()

    e = []
    lst = []

    for i in range(0, len(questions) - 1):
        for k,v in questions.items():
            query = (k,v)
            answer = answers[i]
            q = (query, answer)
            e.append(q)
            lst.append(i)

    shuffled = []

    while len(lst) - 1 > 0:
        num = secrets.randbelow(len(lst) - 1)
        j = lst.pop(num)
        shuffled.append(e[j])
    
    return shuffled

def createQ(text, num):
    # questions choices answers
    # Q = QC[0]
    # C = QC[1]   
    QCA = text[0]
    QC = QCA[0]
    A = QCA[1]

    question = Question(QC, A)

    return question