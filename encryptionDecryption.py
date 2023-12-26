from keys import encryptionKey,decryptionKey

def encryption(EnteredString,encryptionKey,decryptionKey):
    encryptedList = []
    encryptString = ""
    for item in EnteredString:
        for item2 in encryptionKey:
            if item == item2:
                index = encryptionKey.index(item2)
                encryptedList.append(decryptionKey[index])
    encryptString = encryptString.join(encryptedList)
    return encryptString
    
def decryption(EnteredString,encryptionKey,decryptionKey):
    decryptedList = []
    decryptString = ""
    for item in EnteredString:
        for item2 in decryptionKey:
            if item == item2:
                index = decryptionKey.index(item2)
                decryptedList.append(encryptionKey[index])
    decryptString = decryptString.join(decryptedList)
    return decryptString

while True:
    userInput = input("For encryption type 'e' and for decryption type 'd'\n")
    userInputUpper = userInput.upper()
    
    if userInputUpper == 'E' or userInputUpper == 'D':
        entryFlag = ""
        if userInputUpper == 'E':
            entryFlag = "Encryption"
        else:
            entryFlag = "Decryption"

        userInput2 = input(f"Please enter the String for {entryFlag}\n")
        userInput2Upper = userInput2.upper()
        if userInputUpper == 'E':
            returnedValue = encryption(userInput2Upper,encryptionKey,decryptionKey)
            print(returnedValue)
        else:
            returnedValue = decryption(userInput2Upper,encryptionKey,decryptionKey)
            print(returnedValue)
    else:
        print("Invalid Entry\n")
    wannaContinue = input("If you want to continue press 'c' press any other key to stop\n")
    wannaContinueUpper = wannaContinue.upper()
    if wannaContinueUpper != 'C':
        break


