with open("C:/Users/Sahith/Downloads/CommonWords.txt") as file_in:
    data = file_in.read().split()

letters = input("Letters: ")
res = [letters[i: j] for i in range(len(letters))
          for j in range(i + 1, len(letters) + 1)]

for i in res:
    if i in data and len(i) >= 2:
        print(i)