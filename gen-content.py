def main():

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
    
    dictQ = {}

    for each in sortd:
        size = len(each)
    


if __name__ == "__main__":
    main()