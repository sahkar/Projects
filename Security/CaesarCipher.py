from random import randint
from uuid import getnode as get_mac
mac = get_mac()
macString= ":".join(("%012X" % mac) [i:i+2] for i in range (0,12,2))



def checker(num):
    decrpyt = False
    first = org[0]
    if decrpyt == False:
        shift = (ord(org[0])-num)
        for i in range (0, len(org)):
            if ord(org[i]) != 32:
                org[i] = ord(org[i])-shift
                if org[i] < 33:
                    org[i] = org[i]+94
                org[i] = chr(org[i])
           
        last = org[0]
        final = "".join(org)
        print(final)
        check = input("Does the phrase make sense? If yes, then you are looking at the decrypted phrase. If no, sorry about that, we'll try again.\n")
        if check == "yes":
            print("Decrypted cipher: " + final)
            shift = ord(last) - ord(first)
            print(str(shift))
            decrpyt = True
    return decrpyt

choice = input("Enter 1 if you would like to encrypt text or 2 if you would like to decrypt text. \n")

if choice == "1":
    org = input("Enter text to encrypt it. \n")
    org = list(org)
    numPrompt = input("Enter a shift number. If you would like to randomize it , type random.\n")

    if numPrompt == "random":
        shift = randint(1,26)
    else:
        shift = int(numPrompt)

    for i in range (0, len(org)):
        if ord(org[i]) != 32:
            org[i] = ord(org[i])+shift
            if org[i] > 126:
                org[i] = org[i]-94
            org[i] = chr(org[i])

    final = "".join(org)
    print(final)

if choice == "2":
    if macString == "C8:34:8E:11:D1:44":
        org = input("Enter text to decrypt it. \n")
        org = list(org)
        promptShift = input("Enter the shift value. If you do not know the shift value enter idk \n")
        if promptShift != "idk":
            shift = int(promptShift)
            for i in range (0, len(org)):
                if ord(org[i]) != 32:
                    org[i] = ord(org[i])-shift
                    if org[i] < 33:
                        org[i] = org[i]+94
                    org[i] = chr(org[i])

            final = "".join(org)
            print(final)
        elif promptShift == "idk":
            for i in range (97,122):
                if checker(i):
                    break
    else:
        print("You do not have decryption authorization.")
        quit()
 
    
        


    

