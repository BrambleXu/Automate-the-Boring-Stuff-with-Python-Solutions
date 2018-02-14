# Regex Version of strip()
import re

def regex_strip(string, rm_str=None):
    if rm_str == None:
        return string.strip()
    else:
        string = string.strip()
        string_regex = re.compile(rm_str)
        return string_regex.sub('', string)


if __name__ == '__main__':
    string = input('Enter a string: ')
    rm_str = input('Enter the str you want to remove from the string or just clik enter: (Optional)')
    string = regex_strip(string, rm_str)
    print (string)
