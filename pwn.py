def pwn(files, text):
    if files:
        with open(files, 'r') as f:
            chal = f.read()
    if text:
        #print("Text arument was reached in pwn")