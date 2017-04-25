# This code will resolve the comfusion between lambdas and functools.partial in python
# <Author>Birbal Srivastava</Author>
from functools import partial

def multiply(x,y):
    return x*y

def lambdademo():
    multiple_of = 3
    func = lambda x : multiply(multiple_of,x)
    print('func(2) returns: ',func(2), 'expected return is 6')
    multiple_of = 4
    print("Changing multiple_of DOES make an impact here")
    print('func(2) returns: ', func(2), 'expected return is 8')

def partialdemo():
    multiple_of=5
    func = partial(multiply,multiple_of)

    print('func(2) returns: ', func(2), 'expected return is 10')

    multiple_of = 7

    print("Changing multiple_of DOESN'T impact here")
    print('func(3) returns: ', func(3), 'expected return is 15')

def main():
    lambdademo()
    partialdemo()


if __name__ == '__main__':
    main()

