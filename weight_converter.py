weight = input("Weight:\n")
_type = input("Convert to (K)g or (L)b?:\n")

if _type.upper() == "L":
    answer = float(weight) * 2.2
    print(f"convert = {answer}") 

elif _type.upper() == "K": 
    answer = float(weight) * 0.45
    print(f"convert = {answer}")