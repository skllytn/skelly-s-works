# formula = kg/m^

def bmi_calc(bmi: float):
    weight = float(input("Please input your weight (kg):\n"))
    height = float(input("Please input your height (m):\n"))
    height2 = height * height
    bmi = weight / height2

    if bmi <= 18.4:
        print("You are underweight :(")

    elif bmi > 18.5 and bmi <= 24.9:
        print("You are a normal weight WOOO!!")

    elif bmi > 25 and bmi <= 39.9:
        print("You are overweight, stinkyyyy")

    elif bmi >= 40:
        print("You are MF OBESEEEEEE GAH DAYUMMMM")

mode = input("Do you measure in imperial or metric:\n")

if mode == "imperial":
        print("Stupid fucking american")

elif mode == "metric":
    weight = float(input("Please input your weight (kg):\n"))
    height = float(input("Please input your height (m):\n"))
    height2 = height * height
    bmi = weight / height2

    if bmi <= 18.4:
        print("You are underweight :(")

    elif bmi > 18.5 and bmi <= 24.9:
        print("You are a normal weight WOOO!!")

    elif bmi > 25 and bmi <= 39.9:
        print("You are overweight, stinkyyyy")

    elif bmi >= 40:
        print("You are MF OBESEEEEEE GAH DAYUMMMM")

else:
    print("Error, learn to fucking spell.")