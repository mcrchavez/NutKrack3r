#!/usr/bin/env python3

import click
import os.path
from crypto import *
from pwn import *


valid_categories = ('crypto', 'pwn', 'web', 'rev', 'forensics', 'osint')

@click.command()
@click.option('--category', help = 'Define category (crypto, pwn, web, rev, forensics, osint)')
@click.option('--text', default = '', help = 'CTF text inputs')
@click.option('--files', default = '', help = 'CTF file inputs (File mqust be in same directory)')
@click.option('--fformat', default = '', help= 'Provide with CTF flag format to be set as default')
def main(category, text, files, fformat):
    if category not in valid_categories:
        print('Error: Category not valid, see --help')
        return 1
    if files == '' and text == '':
        print('Error: Need input, see --help')
        return 2
    elif text == '':
        if not os.path.exists(files):
            print('Error: File does not exist, see --help')
            return 3
    if fformat:
        #print(f"fformat input: {fformat}")
        #write the fformat striing to file to be stored
        with open("flagformat.txt", 'w') as flagfile:
            flagfile.write(fformat)
            flagfile.close()

    with open("flagformat.txt", 'r') as flagfile:
        flagformat = flagfile.read()
        if flagformat == r"defaultFlagFormat{}":
            #if the flag was never set other that default with --fformat
            #just provide the module with an empty string
            flagformat = ''
            print("Flagformat set to default resolving to empty string")
        flagfile.close()

    #blacklisting dangerous charecters before feeding into exec()
    blacklist = ['"', "'", '(', ')', ';']
    for char in blacklist:
        if (char in files) or (char in text):
            print('Exiting -- dangerous char in inputs')
            return 4

    #insecure due to file name command injection but secure implementation of this would be nice
    execute = category + f'("{files}", "{text}")'
    #uncomment for exec () debug print("Debug execute var: " + execute)
    exec(execute)

if __name__ == '__main__':
    main()
