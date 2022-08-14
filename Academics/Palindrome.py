checking =True

while checking == True:
    word = input("Enter a word to check if it is a palindorme. \n")
    word_check =word[::-1]

    if word == word_check:
        print('True')

    elif word != word_check:
        print('False')
