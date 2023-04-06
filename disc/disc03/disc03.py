def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
      k = 2
      def prime_helper(n, k):
        if k == n:
            return True
        elif n % k == 0:
            return False
        else:
            return prime_helper(n, k + 1)
      return prime_helper(n, k)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    steps = 1
    def helper(n, steps):
        print(n)
        if n == 1:
            return steps
        else:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1 
            return helper(n, steps + 1)
    return helper(n, steps)

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    # def get_last(n):
    #     return n % 10

    # res = 0
    # step = 0
    # def helper(n1, n2, res, step):
    #     if n1 == 0 and n2 == 0:
    #         return res 
    #     else: 
    #         if n1 == 0 or n2 == 0:
    #             min_n, max_n = min(n1, n2), max(n1, n2)
    #             last = get_last(max_n)
    #             max_n = max_n // 10
    #             res = last * 10**step + res
    #             return helper(min_n, max_n, res, step+1)
    #         else:
    #             last1, last2 = get_last(n1), get_last(n2)
    #             if last1 <= last2:
    #                 last = last1
    #                 n1 = n1 // 10
    #             else:
    #                 last = last2
    #                 n2 = n2 // 10
    #             res = last * 10**step + res
    #             return helper(n1, n2, res, step+1)

    # return helper(n1, n2, res, step)
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 <= n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
