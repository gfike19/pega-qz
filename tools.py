from genContent import getAnswers, getQuestions
from question import Question
import secrets

def getShuffled():
    answers = getAnswers()
    questions = getQuestions()

    e = []
    lst = []

    for i in range(0, len(questions) - 1):
        query = questions[i]
        ans = answers[i]
        q = Question(query, ans)
        e.append(q)
        lst.append(i)

    shuffled = []

    while len(lst) > 0:
        num = secrets.randbelow(len(lst) - 1)
        j = lst.pop(num)
        shuffled.append(e[j])
    
    return shuffled

