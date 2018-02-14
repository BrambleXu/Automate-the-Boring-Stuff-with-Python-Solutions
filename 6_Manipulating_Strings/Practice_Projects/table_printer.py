


def column_wideth(tabel):
    colWideths = [0] * len(tabel)
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if len(tabel[i][j]) > colWideths[i]:
                colWideths[i] = len(tabel[i][j])
    return colWideths



def print_table(table, colWideths):
    for i in range(len(table[0])): # i = 4 meansing the output has 4 rows
        #print (i)
        for j in range(len(table)): # j = 3 to output each row
            print (table[j][i].rjust(colWideths[j]), end=' ')
        print ()


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

    colWideths = column_wideth(tableData)
    print_table(tableData, colWideths)
