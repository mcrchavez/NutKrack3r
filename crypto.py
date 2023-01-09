#define the flagText which cipher is looking for in temporrary constant
#will likely get this string from a file with flag format
flagText = 'pp'
successString = '---Possible Flag Found!!!---'
failureString = '---Unable to Find Flag---'


def crypto(files, text):
    #Unsure what to do with multiple inputs at once

    if files:
        with open(files, 'r') as f:
            chal = f.read()
    if text:
        chal = text

    caesar(chal)


def caesar(chal):
    found = False
    tmp = ''
    rotated = []
    for key in range(0,26):
        for char in chal.upper():
            tmp += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        rotated.append(tmp)
        tmp = ''
    for attempt in rotated:
        if flagText in attempt:
            print(successString)
            print(attempt)
            found = True
    if not found:
        print(failureString)


    
            