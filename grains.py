def square(number):
    if number>0 and number<=64:
        return pow(2,(number-1))
    else:
        raise ValueError("square must be between 1 and 64")
def total():
    return pow(2,64)-1