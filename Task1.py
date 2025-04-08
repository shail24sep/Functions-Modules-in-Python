x=int(input("Enter a number:"))

def factorial(n):
    if n<2:
        return 1
    else:
        return n *(factorial(n-1))

y=factorial(x)
print("Factorial of",x,"is:",y)