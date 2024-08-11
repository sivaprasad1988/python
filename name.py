def calculate_love_score(name1, name2):
    nameString = name1 + name2
    checkStrings = ["true", "love"]

    i = 0
    score = ""
    for checkString in checkStrings:
        checkList = []
        for checkChar in checkString.lower():
            charCount = nameString.count(checkChar)
            if charCount > 0:
                checkList.append(charCount)
        score += str(sum(checkList))
        i += 1
    print(score)




calculate_love_score('Angela Yu', "Jack Bauer")
