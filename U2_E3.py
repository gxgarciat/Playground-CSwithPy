def main():

    """
    Write an iterative function iterPower(base, exp) that calculates the e
    xponential  by simply using successive multiplication.

    This function should take in two values - base can be a float or an integer;
    exp will be an integer  0. It should return one numerical value.
    The code must be iterative - use of the ** operator is not allowed.
    """

    def iterPower(base, exp):

        power = base

        if exp > 0:
            for i in range(exp-1):
                power = base*power
        else:
            power = 1

        return power



if __name__ == "__main__":
    main()
