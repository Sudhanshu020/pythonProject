def return_factor(num: int):
    for i in range(1 , num+1):
        if (num % i == 0):
            print (i)


n = int(input("enter a number to find the factors:"))
return_factor(n)
