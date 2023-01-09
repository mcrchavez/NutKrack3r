def forensics(files, text):
    if files:
        with open(files, 'r') as f:
            chal = f.read()
    if text:
        chal = text