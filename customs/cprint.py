import time

def show(*args, delay: int):
    """"this function prints the provided data 
    it takes two arguments, one is *args and one more delay
    delay is an keyword argumet """
    for line in args:
        for char in line:
            print(char, end="", sep="")
            time.sleep(delay)
        print()