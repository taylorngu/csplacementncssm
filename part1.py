#5

def cube(x):
    return x ** 3

#6

if x == y:
    

#7

def test(x):

    if (x ** 2 > 500 and 3 * x < 1000 and 4 * x + 2 < 1050):
        return True
    else:
        return False

#8

def first_letter(arr):

    letters = "";

    for word in arr:
        letters += word[0]

    return letters

#9 - Instructions unclear on whether there are 3 or 4 arguments, and the
#    value of x

def f(a, b, n):

    total = 0
    step = (b - a) / (n + 1)
    
    for num in range(n + 1):
        total += a ** 3
        a += step

    return total / (n+1)

#10

def contains(s1, s2):

    if s2 in s1:
        return True
    else:
        return False
    
