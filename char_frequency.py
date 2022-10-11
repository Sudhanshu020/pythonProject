def char_frequency(str1):
    n = len(str1)
    i = 0
    while i < n - 1:
        c = 1
        while (i < n - 1 and str1[i] == str1[i + 1]):
            c += 1
            i += 1
        i += 1
        print(str1[i - 1] + str(c), end="")

str1 = input("enter a string:")
char_frequency(str1)