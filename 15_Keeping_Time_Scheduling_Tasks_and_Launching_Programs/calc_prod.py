import time
def calc_prod():
    # Calculate the product of the first 100.000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (end_time - start_time))
