translate = {
     'a': 12,
     'b': 211,
     'c': 2121,
     'd': 211,
     'e': 1,
     'f': 1121,
     'g': 221,
     'h': 1111,
     'i': 11,
     'j': 1222,
     'k': 212,
     'l': 1211,
     'm': 22,
     'n': 21,
     'o': 222,
     'p': 1221,
     'q': 2212,
     'r': 121,
     's': 111,
     't': 2,
     'u': 112,
     'v': 1112,
     'w': 122,
     'x': 2112,
     'y': 2122,
     'z': 2211,
     '1': 12222,
     '2': 22111,
     '3': 11122,
     '4': 1112,
     '5': 11111,
     '6': 21111,
     '7': 22111,
     '8': 22211,
     '9': 22221,
     '0': 22222,
     ' ': 0
}
choice = input("Enter '1' for English to Morse Code and '2' for Morse Code to english \n")

if choice == '1':
     a = input('Enter text to convert to morse code. \n')
     a = a.lower()
     a = list(a)
     for i in range (0, len(a)):
          a[i] = str(translate[a[i]])
     a = '/'.join(a)
     print(a)
if choice == '2':
     a = input('Enter morse code to convert to text. \n')
     a = list(a)
     for i in range (0, len(a)):
          x = list(translate.values)
          a[i] = str(x[i])  
     a = '/'.join(a)
     print(a)