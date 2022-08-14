source = 'word'
target = list("*"  *len(source))
print(target)

guessing = True
while guessing:
    guess = input('Guess a letter from a-z: ')
    
    index = 0
    while index < len(source) :
        if source[index] == guess:
            target[index] = guess
            print(target)
        index += 1

    if source == ''.join(target):
        guessing = False
        print ('You succeeded')