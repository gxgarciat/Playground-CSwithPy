def main():

    """
    Assume s is a string of lower case characters.
    Write a program that prints the number of times the string 'bob' occurs in s.
    For example, if s = 'azcbobobegghakl', then your program should print
    Number of times bob occurs is: 2
    """

    numBob = 0
    i = 0

    for letters in s:
        if i < (len(s)-2):
            if letters == 'b':
                if s[i+1] == 'o':
                    if s[i+2] == 'b':
                        numBob += 1
        i = i +1


    print('Number of times bob occurs is: ' + str(numBob))

if __name__ == "__main__":
    main()
