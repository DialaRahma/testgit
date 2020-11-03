def fak(x):

    if(x == 0):
        return 1
    else:
        return x*fak(x-1)


print(f"Factorial of 2 is {fak(2)}")
print(f"Factorial of 3 is {fak(3)}")
print(f"Factorial of 5 is {fak(5)}")
print(f"Factorial of 6 is {fak(6)}")
