
def collatz(number):
    return number // 2 if (number % 2) == 0 else number * 3 + 1

if __name__ == '__main__':
    print ('Enter a number greater than one: ')
    try:
        number = int(input())
        while True:
            if number != 1:
                number = collatz(number)
                print (number)
            else:                
                break
    except:
        print ('Error: Invalid Value. You did not enter an integer.')
