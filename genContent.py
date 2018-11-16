# gets everything from text file
content = None
with open("content-formatted.txt") as f:
    content = f.readlines()
    content = [x.strip("\n") for x in content] 

# empty line is the delineator between questions
sortd = []
temp = []
for line in content:
    if line != "":
        temp.append(line)
    else:
        sortd.append(temp)
        temp = []

# pulls the answers into a separate list
answers = []
for lines in sortd:
    for each in lines:
        try:
            i = int(each[0])
            answers.append(each)
        except Exception:
            # does nothing
            pass

# put questions and options into a list
notA = []
for line in sortd:
    temp = []
    for each in line:
        if each not in answers:
            temp.append(each)
    notA.append(temp)

# convert notA into dictionary form, much easier to handle than a list
questions = {}

for each in notA:
    sz = len(each) -1
    temp = []
    while sz > 0:
        temp.append(each[sz])
        sz -= 1
    questions[each[0]] = temp

# formats the answers so that the nunbers are in a separate list in a tuple with the text
formatted = []
for item in answers:
    options = []
    text = ""
    for char in item:
        if char.isdigit():
            options.append(char)
        else:
            text += char
    formatted.append((options, text))

# removes commas from answer text
finalAnswers = []
for each in formatted:
    comsCount = len(each[0])
    temp2 = each[comsCount:len(each[1])]
    temp1 = each[0]
    finalAnswers.append((temp1, temp2))

def getQuestions():
    return questions

def getAnswers():
    return finalAnswers

# returns type tuple
# print(type(questions.items()[0]))