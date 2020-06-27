from collections import deque
from itertools import permutations
from itertools import combinations
from math import sqrt

# taking single input
input()

# taking 1 to n number of inputs inputs in single line
x1, x2, xN = map(int, input().split())

# taking multiple inputs in single line
x = []
x = [int(x) for x in input().split()]


# list
thislist = []
thislist.append()  # to append element with value at end
thislist.insert()  # to insert element at index
thislist.count()  # to count occurence of certain value
sum(thislist)  # to calc the sum of all elements present
thislist.index()  # to give index of first occurence of certain value
min(thislist)
max(thislist)
reverse(thislist)  # reverses the list
thislist.sort()
thislist.sort().reverse()  # reverses the sorted list

# to remove a element using index
thislist.pop(index)
del thislist.(index)
# to remove element using value
thislist.remove()


# deque
de = deque([])
de.append()
de.appendleft()
de.pop()
de.popleft()
de.index(ele, beg, end)
de.insert(index, ele)
de.count(ele)
de.extend([])
de.extendleft([])
de.rotate(2)  # rotate by 2 to right
de.reverse()


def isPrime(n):

    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(sqrt(n))+1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print i,
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print n
