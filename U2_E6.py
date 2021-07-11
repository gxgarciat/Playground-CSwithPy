def main():

    """
    The greatest common divisor of two positive integers is the largest integer
    that divides each of them without remainder. For example, gcd(2, 12) = 2

    Write a function, gcdRecur(a, b), that implements this idea recursively.


    """

    def gcdRecur(a, b):

        if b == 0:
            return a
        else:
            return gcdRecur(b, a % b)


if __name__ == "__main__":
    main()
