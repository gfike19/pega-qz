from genContent import getQuestions
import secrets

def getShuffled():
    qs = getQuestions()
    limit = len(qs)
    lst = []

    for num in range(0, limit):
        lst.append(num)
    
    newLst = 