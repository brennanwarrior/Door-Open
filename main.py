# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from smith_script import do_math
from servo import open_door
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
while True:
    print_hi('PyCharm')
    number = input("Enter Number")
    number = int(number)
    # do_math(number)
    if number ==2:
        print("open door")
        open_door()
pwm.stop()
GPIO.cleanup()
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
