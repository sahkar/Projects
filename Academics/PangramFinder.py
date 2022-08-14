import itertools


with open("C:/Users/Sahith/Downloads/CommonWords.txt") as file_in:
    data = file_in.read().split()

def allPermutations(num):
    permList = list(itertools.permutations(newLetters,num))
    for i in range(0,len(permList)):
        permList[i] = "".join(permList[i])
    return permList

def findWords(permList):
    wordList = []
    for word in permList:
        if word in data and letters[len(letters)-1] in word:
            wordList.append(word)
    return wordList

    


letters = input("Enter today's letters: ")
newLetters = letters*3

allWords = []
j = len(newLetters)
for j in range(4,len(newLetters)):
    permList = allPermutations(j)
    print(permList)
    wordList = findWords(permList)
    allWords += wordList

print(allWords)


