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


