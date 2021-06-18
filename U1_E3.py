def main():

    """
    Write a while loop that sums the values 1 through end, inclusive.
    Ex.: 1 + 2 + 3 + 4 + 5 + 6.
    Ans. 21

    :return:
    """
    end = 6  # Based on the example

    i = 0
    total = 0
    while i < end:
        i = i + 1
        total = i + total

    print(total)

if __name__ == "__main__":
    main()