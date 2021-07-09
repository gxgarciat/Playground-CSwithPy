def main():

    """
    Create a program that guesses a secret number!
    The program works as follows: the user thinks of an integer between 0
    (inclusive) and 100 (not inclusive). The computer makes guesses, and the user
     gives it input - is its guess too high or too low?
     Using bisection search, the computer will guess the user's secret number!
    """


    random1 = 50
    low = 0
    high = 100

    print('Please think of a number between 0 and 100!')



    while True:
        print('Is your secret number ' + str(random1)+'?')
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if guess == 'c':
            print('Game over. Your secret number was:  ' + str(random1))
            break

        while guess != 'h' and guess != 'l':
            print('Sorry, I did not understand your input.')
            print('Is your secret number ' + str(random1) + '?')
            guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

        if guess == 'h':
            high = random1
            random1 = int(abs((high+low)/2))
        else:
            low = random1
            random1 = int(abs((high+low)/2))

if __name__ == "__main__":
    main()
