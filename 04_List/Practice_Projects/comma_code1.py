def list2str(row_list):
    output = ''
    for i in range(len(row_list)):
        if i != len(row_list) - 1:
            output += str(row_list[i]) + ', '
        else:
            output += 'and ' + str(row_list[i])
    return output

if __name__ == '__main__':
    row_list = ['apples', 'bananas', 'tofu', 'cats']
    print (list2str(row_list))
    
