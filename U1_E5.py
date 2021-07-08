def main():

    """
    Assume s is a string of lower case characters.
    Write a program that prints the longest substring of s in which the letters
    occur in alphabetical order. For example, if s = 'azcbobobegghakl',
    then your program should print Longest substring in alphabetical order is: beggh
    In the case of ties, print the first substring. For example, if s = 'abcbcd',
    then your program should print Longest substring in alphabetical order is: abc
    """

    longstr = ''
    temp1 = ''

    for i in range(len(s)):
        temp1 = temp1 + s[i]
        if i > len(s)-2:
            break

        if len(temp1) > len(longstr):
            longstr = temp1

        if s[i] > s[i+1]:
            temp1 = ''

    if longstr[len(longstr) - 1] == s[len(s) - 2]:
        if len(longstr) < len(temp1):
            if s[len(s) - 1] >= s[len(s) - 2]:
                longstr = longstr + s[len(s) - 1]

    print('Longest substring in alphabetical order is: ', longstr)


if __name__ == "__main__":
    main()
