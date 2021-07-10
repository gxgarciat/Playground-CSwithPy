def main():

    """
    The greatest common divisor of two positive integers is the largest integer
    that divides each of them without remainder. For example, gcd(2, 12) = 2

    Write an iterative function, gcdIter(a, b), that implements this idea.
    

    """

    def gcdIter(a, b):
        div_A = []
        div_B = []
        for i in range(a,0,-1):
            if a%i == 0:
                 div_A.append(i)


        for i in range(b, 0, -1):
            if b % i == 0:
                 div_B.append(i)

        div_C = div_A + div_B
        duplicates =[]
        div_C.sort()

        for i,j in enumerate(div_C):
            if (i>0) and (div_C[i]==div_C[i-1]):
                duplicates.append(j)
        if len(duplicates) >= 2:
            return max(duplicates)
        else:
            return min(duplicates)

if __name__ == "__main__":
    main()
