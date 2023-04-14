def countWords():
    fileName = input("enter file name: ")
    number = 0
    file = open(fileName,"r")
    for line in file: 
        words = line.split()
        number = number+len(words)
    print("number of words: ")
    print(number)

countWords()