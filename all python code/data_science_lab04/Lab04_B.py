import numpy as np
from random import randrange


A = np.linspace(5, -5, 51)

B = np.logspace(0, 1, num=101) #  or np.geomspace(1, 10, num=101)

C = np.arange(1,101).reshape(10,10).T

d = np.arange(1,13)
D = d*d.reshape(12,1)

def E(X):
    return X[::2, ::2]

def F(X):
    return X[1:-1, 1:-1]

def G(X):
    # The shape of return value will be (M, 2)
    M = X.shape[1]
    d1 = X[range(1,M), range(M-1)]
    d2 = X[range(M-1), range(1,M)]

    return np.vstack((d1, d2)).T


# Do NOT modifiy the main function
def main():
    print('A: \n', A, '\n')
    print('B: \n', B, '\n')
    print('C: \n', C, '\n')
    print('D: \n', D, '\n')

    M = randrange(3, 8)
    X = np.random.randint(10, size=(M, M))

    print('X: \n', X, '\n')
    print('E: \n', E(X), '\n')
    print('F: \n', F(X), '\n')
    print('G: \n', G(X), '\n')


if __name__ == "__main__":
    main()