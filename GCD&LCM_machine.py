x = 0
y = 0
questionx = "Insert value for the first number:" 
questiony = "Insert value for the second number:" 

def error(z , question):
    try:
        z = int(input(f"{question} \n"))
    except ValueError:
        print("\nThe number needs to be a whole number!!!")
        return error(z , question)

    if z <= 0:
        print("\nThe number can't be equal or less than 0!")
        return error(z , question)

    return z
    


x = error(x , questionx)
y = error(y , questiony)

x_end = x
y_end = y

while x != 0 and y != 0:
    if x > y:
        x %= y
    else:
        y %= x

if x == 0:
    print(f"\nThe GCD of {x_end} and {y_end} is: {y}")
    print(f"\nThe LCM of {x_end} and {y_end} is: {(x_end * y_end) // y }")
else:
    print(f"\nThe GCD of {x_end} and {y_end} is: {x}")
    print(f"\nThe LCM of {x_end} and {y_end} is: {(x_end * y_end) // x }")


