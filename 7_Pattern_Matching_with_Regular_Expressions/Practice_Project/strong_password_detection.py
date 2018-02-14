'''
A strong password is defined as one

that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.

You may need to test the string against multiple regex patterns to validate its strength.
'''
import re

def password_detection(pw):
    if re.match(r'[a-zA-Z0-9]{8,}', pw):
        return True
    else:
        return False

if __name__ == '__main__':
    pw = input('Enter your password: ')
    #print (pw)
    if password_detection(pw):
        print ('Good, your password is strong!')
    else:
        print ('The password is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.')
