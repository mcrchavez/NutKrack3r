def crypto(files, text):
    #Unsure what to do with multiple inputs at once
    if files:
        with open(files, 'r') as f:
            chal = f.read()
    if text:
        chal = text

    caesar(chal)


def caesar(chal):
    tmp = ''
    rotated = []
    for key in range(0,26):
        for char in chal.upper():
            tmp += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        rotated.append(tmp)
        tmp = ''
    for attempt in rotated:
        if 'FLAG' in attempt:
            print(attempt)