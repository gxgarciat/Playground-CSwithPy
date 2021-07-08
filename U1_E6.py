def main():

    """
    Assume s is a string of lower case characters.
    Write a program that counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
    if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
    """

    numVow = 0

    for letters in s:

        if letters == 'a':
            numVow = numVow + 1
        elif letters == 'e':
            numVow = numVow + 1
        elif letters == 'i':
            numVow = numVow + 1
        elif letters == 'o':
            numVow = numVow + 1
        elif letters == 'u':
            numVow = numVow + 1

    print('Number of vowels:  ' + str(numVow))

if __name__ == "__main__":
    main()
