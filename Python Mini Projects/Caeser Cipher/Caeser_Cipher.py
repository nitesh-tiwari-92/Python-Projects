

import string

lst = list(string.ascii_uppercase)

con = 'y'

while con in ['y', 'yes', 'ye']:

    typ = input('\nType \'encrypt\' for encription, type \'decrypt\' for decription: ')
    inc = ''

    if typ in ['encrypt', 'e', 'enc', 'en']:

        _str = input('\nEnter the alphabetical string which you want to encrypt: ').upper()
        ch = int(input('\nEnter the number with which you want to decript the string: '))

        for i in _str:

            if not i.isspace() and i in lst:

                for l in lst:

                    if i == l:

                        inc += lst[(lst.index(i) + ch) % 26]
                        

            elif not i.isspace() and i not in lst:

                inc += i

            else:

                inc += ' '

        print(f'\nHere is the encrypted message: {inc.lower()}')

    else:
        
        dec = ''
        _str = input('\nEnter the alphabetical string which you want to decrypt: ').upper()
        ch = int(input('\nEnter the number with which you want to decript the string: '))
        
        for s in _str:

            if not s.isspace() and s in lst:

                dec += lst[(lst.index(s) - ch) % 26]

            elif not s.isspace() and s not in lst:

                dec += s

            else:

                dec += ' '

        print(f'\nDecrypted Message: {dec.lower()}')

    con = input('\nType \'yes\' if you want to go again. Otherwise type \'no\': ').lower()

print('\nGood Bye!!')