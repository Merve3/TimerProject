# import the time module
import time

# define the countdown func.
def countdown(counter):
    while counter:
        mins, secs = divmod(counter, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        counter -= 1

    print(time_input + " seconds is over")


# input time in seconds 
time_input = input("Enter the time in seconds: ")

# function call 
countdown(int(time_input))