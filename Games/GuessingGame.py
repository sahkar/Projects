from random import randint

def values(c):
    return {c:randint(0,9)}

#letters = input('Enter four letters: ')
letters = "a,b,c,d"
letters = letters.split(',')

for i in range(0,4):
    c = letters[i]
    print(c + ':' + str(values(c)[c]))
    