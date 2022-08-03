# formula = Fn = Fn-1 + Fn-2

def Fibonacci(n):

    if n < 0:
        print("Invalid input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
        
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)



mode = input("Do you want to output:\n"
             "1.)a specific term.\n"
             "2.)a range.\n")

if mode == "1":
    n = int(input("Please input your desired term:\n"))
    print(Fibonacci(n))

if mode == "2":

    for n in range(1, 20 + 1):
        print(Fibonacci(n))