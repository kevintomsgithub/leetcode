array = [i for i in range(10)]

def find_square(array):
    yield 'First'
    for i in array:
        yield i*i
    yield 'Yes'


for i in find_square(array):
    print(i)