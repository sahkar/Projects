import random
with open("C:/Users/Sahith/Downloads/CommonWords.txt") as file_in:
    data = file_in.read().split()

word = ""
points = 0
while len(word) != 7:
    word = data[random.randint(1,100000)] 
word = list(word)
random.shuffle(word)
word = "".join(word)

entries = []

while True:
    print(word)
    guess = input("Enter a word: \n")
    if len(guess) <4:
            print("Guess too short\n")
    elif guess in entries:
        print("Already found\n")
    elif len(guess) >=4 and guess in data:
        for i in guess:
            if i not in word:
                print("Invalid letters\n")
                break
        else:
            if len(guess) == 4:
                points = points +1
            else:
                points = points + len(guess)
            entries.append(guess)
            print("Points: " + str(points)+"\n")
    else:
            print("Guess not in dictionary \n")