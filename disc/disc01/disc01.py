def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    # if temp < 60 or raining:
    #     return True
    # else:
    #     return False
    return True if temp <60 or raining else False

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    def result(num):
        res = num
        if num % 3 == 0:
            res = 'fizz'
        if num % 5 == 0:
            res = 'buzz'
        if num % 3 == 0 and num % 5 == 0:
            res = 'fizzbuzz'
        return res

    for i in range(1, n + 1):
        res = result(i)
        print(res)