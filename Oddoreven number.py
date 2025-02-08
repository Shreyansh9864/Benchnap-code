# Hello guy today I am gona make a prog on odd or Even
# 1. Create a function
def odd_and_function():
    try:
        user = int(input("Enter a number \n"))

    except ValueError:
        print("Must be a integer")

    if user % 2 == 0:
        print("It is an even number")

    else:
        print("It is a odd number")

odd_and_function()
