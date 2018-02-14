# phone_and_email.py - Finds phone numbers and email addresser on the clipboard.

'''
For example, your phone and email address extractor will need to do the following:

    Get the text off the clipboard.

    Find all phone numbers and email addresses in the text.

    Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The code will need to do the following:

    Use the pyperclip module to copy and paste strings.

    Create two regexes, one for matching phone numbers and the other for matching email addresses.

    Find all matches, not just the first match, of both regexes.

    Neatly format the matched strings into a single string to paste.

    Display some kind of message if no matches were found in the text.
'''

import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first 3 digits
    (\s|-|\.)?              # separator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )''', re.VERBOSE)

# TODO: Create email regex

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# TODO: Find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        pnone_num += ' x' + groups[6]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print ('Copied to clipboard')
    print ('\n'.join(matches))
else:
    print ('No phone number or email address found.')
