with open("C:/Users/Sahith/Downloads/CommonWords.txt") as file_in:
    data = file_in.read().split()

letters = input("Enter today's letters: ")
words = []
temp = 0
for word in data:
    for letter in word:
        if letter in letters:
            pass
        else:
            temp = 1  
            break
    if temp == 1:
        temp = 0
        continue
    else:
        if letters[len(letters)-1] in word and len(word) > 3:
            words.append(word)

words = sorted(words, key=len)
for cWord in words:
    print(cWord)    