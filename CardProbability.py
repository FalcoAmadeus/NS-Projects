@@ -0,0 +1,34 @@
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
### from https://stackoverflow.com/a/4941932

x = int(input("Insert Deck Size: "))
y = int(input("Insert amount of card's copies: "))
z = int(input("Insert starting hand size: "))
w = int(input("Insert number of successes: "))
first = ncr(y, w)*ncr((x-y), (z-w))/ncr(x, z)
list = [first]
play = True
while play == True:

    if y >=1:
        w = (w+1)
        second = ncr(y, w)*ncr((x-y), (z-w))/ncr(x, z)
        list.insert(0, second)
        perc = list*100
        third = first*100

        if w == y:
            print(sum(perc))
            play = False

        else:
            if w >= y:
                print(third)
                play = False
