def countOfWords(file):
    words = []

    with open(file, "r") as f:
        for line in f:
            words.extend(line.split())
    
    return len(words)

def countOfLetters(file):
    letters = []
    l = []

    with open(file, "r") as f:
        for line in f:
            letters.extend(line)

    for i in range(len(letters)):
        if letters[i] not in l:
            if letters[i].isalpha():
                l.append(letters[i])

    return len(l)

def countOfSentences(file):
    letters = []

    with open(file, "r") as f:
        for line in f:
            letters.extend(line)

    count = letters.count("?") + letters.count(".") + letters.count("?")

    return count    

def maxLetter(file):
    letters = []
    dct = {}
    with open(file, "r") as f:
        for line in f:
            letters.extend(line)

    for i in range(len(letters)):
        if letters[i].isalpha():
            dct[letters[i]] = letters.count(letters[i])

    items = list(dct.items())
    max = 0
    letter = ""

    for i in range(len(items)):
        if items[i][1] > max:
            max = items[i][1]
            letter = items[i][0]
    if max == 1:
        return 0
    return letter   

def maxWord(file):
    words = []
    dct = {}

    with open(file, "r") as f:
        for line in f:
            words.extend(line.split())

    for i in range(len(words)):
        if words[i].isalpha():
            dct[words[i]] = words.count(words[i])

    items = list(dct.items())
    max = 1
    word = ""

    for i in range(len(items)):
        if items[i][1] > max:
            max = items[i][1]
            word = items[i][0] 
    print(max)
    if max == 1:
        return 0           

    return word
                    




     


    

   

