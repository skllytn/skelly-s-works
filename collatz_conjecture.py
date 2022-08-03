def find_interations(number: int) -> int:
    count = 0

    while number != 1:
        count += 1
        if number % 2 == 0:
            number = number / 2  # type: ignore

        else:
            number = number * 3 + 1
    
    return count

mode = input(
    "Which of these would you like to find out?\n"
    "1. The number of iterations it'll take to get to 1\n" 
    "2. The highest number of iterations it'll take to get to 1 for a range of numbers\n"
    )

if mode == "1":

    number = input("Please input a numerical value for this iteration:\n")
    while not number.isdecimal():
        number = input("Error: please input numerical value:\n")

    number = int(number)

    count = find_interations(number)

    print(f"It took {count} iterations to reach this value: {number}")

elif mode == "2":

    max_number = input("Please provide a number to calculate the highest number of iterations it'll take to get to 1 for every number within it:\n")
    while not max_number.isdecimal():
        max_number = input("Error: please input numerical value:\n")

    max_number = int(max_number)
    # number, number of iterations
    highest = [0, 0]
    
    for number in range(2, max_number + 1):
        iterations = find_interations(number)
        if iterations > highest[1]:
            highest = [number, iterations]

    print(f"The most number of iterations it took to get to 1 was: {highest[0]}, with {highest[1]} iterations.")