# using ast.literal_eval change the input(string) to a list in order to process

import ast

def list2str(row_list):
    output = ''
    for i in range(len(row_list)):
        if i != len(row_list) - 1:
            output += row_list[i] + ', '
        else:
            output += 'and ' + row_list[i]
    return output

if __name__ == '__main__':
    try:
        print ('Enter a list:')
        row_list = ast.literal_eval(input())
        print (list2str(row_list))
    except:
        print ('Error: Invalid Value. You did not enter a list.')
