from random import randint


def getMacAddress():
    from uuid import getnode as get_mac
    mac = get_mac()
    macString= ":".join(("%012X" % mac) [i:i+2] for i in range (0,12,2))
    return macString
    
def encrypt(org,key):
    org = org.split(" ")
    key = key.split(",")
    
    for k in range (0,len(key)):
        key[k] = int(key[k])
    
    times = int(len(org)/len(key))
    key = times*key
    extra = int(len(org)%len(key))
    for g in range(0,extra):
        key.append(key[g])

    for k in range (0,len(key)):
        key[k] = int(key[k])
    for i in range (0,len(org)):
        org[i] = list(org[i])
        shift = key[i]
        key.append(str(shift))
        for j in range (0,len(org[i])):
            (org[i])[j] = ord((org[i])[j])+shift
            (org[i])[j] = chr((org[i])[j])
        org[i] = "".join(org[i])
    org = " ".join(org)
    return org

def decrypt(org,key):
    org = org.split(" ")
    key = key.split(",")

    for k in range (0,len(key)):
        key[k] = int(key[k])
    
    times = int(len(org)/len(key))
    key = times*key
    extra = int(len(org)%len(key))
    for g in range(0,extra):
        key.append(key[g])

    for i in range (0,len(org)):
        org[i] = list(org[i])
        shift = key[i]
        key.append(str(shift))
        for j in range (0,len(org[i])):
            (org[i])[j] = ord((org[i])[j])-shift
            (org[i])[j] = chr((org[i])[j])
        org[i] = "".join(org[i])
    org = " ".join(org)
    return org 


choice = input("Enter 1 if you would like to encrypt text and 2 if you would like to decrypt text. \n")

if choice == "1":
    userInput = input("Enter text to encrypt: \n")
    key = input("Enter an array of numbers to encrypt your text by: \n")
    userInput = encrypt(userInput,key)
    print(userInput)

elif choice == "2":
    if getMacAddress() == "C7:7C:60:93:C0:42":
        userInput = input("Enter text to decrypt: \n")
        key = input("Enter an array of numbers to decrypt your text by: \n")
        userInput = decrypt(userInput,key)
        print(userInput)
    else:
        print("You do not have decryption authority. If you think this might be a mistake, please get in contct with an administrator.")
