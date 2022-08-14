from random import randint

with open("C:/Users/Sahith/Downloads/CommonWords.txt") as file_in:
    data = file_in.read().split()

def validate(word):
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            return False
    return True

def checkWord(word):
    print(word in data)
    return word in data

def checkPos(guess, word):
    output = ""
    for i in range(0, len(guess)):
        if(guess[i] == word[i]):
            output += "\u001b[32m" + guess[i]
        elif(guess[i] in word and guess[i] not in guess[0:i]):
            output += "\u001b[33m" + guess[i]
        else:
            output += "\u001b[0m" + guess[i]
    output += "\u001b[0m\n"
    return output

word = ""
guess = ""

while True:
    word = data[randint(0,99999)] 
    if(len(word) == 5 and validate(word)):
        break

for i in range(6):
    guess = input()
    while(len(guess) != 5):
        guess = input("\u001b[31mEnter a five letter word \n\u001b[0m")
    

    if(guess in data):
        print(checkPos(guess,word))
    else:
        print("\u001b[31mNot a word \n\u001b[0m")

    if(guess == word):
        print("Congrats! The word was " + word)
        quit()
    guess = ""

print(word)

