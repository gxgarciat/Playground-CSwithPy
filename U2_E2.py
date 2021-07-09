def main():

    """
    Write a Python function, fourthPower, that takes in one number and returns
     that value raised to the fourth power.

    Use the square procedure defined in an earlier exercise.

    This function takes in one number and returns one number.
    """


    def fourthPower(x):
        '''
        x: int or float.
        '''

        def square(x):

            squared = x*x

            return squared

        squared = square(x)

        fourth = squared*squared

        return fourth


if __name__ == "__main__":
    main()
