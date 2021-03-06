def main():

    """
    By using recursion, write a function recurPower(base, exp) which computes
    by recursively calling itself to solve a smaller version of the same problem,
    and then multiplying the result by base to solve the initial problem.

    This function should take in two values - base can be a float or an integer;
    exp will be an integer . It should return one numerical value.
    The code must be recursive - use of the ** operator or looping constructs is not allowed.

    """

    def recurPower(base, exp):

        if exp == 0:
            power =1
            return power
        else:
            return base * recurPower(base,exp-1)

if __name__ == "__main__":
    main()
