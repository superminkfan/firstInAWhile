# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from os import walk
import os
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

@print_hi
def val(v: str) -> str:
    return 'v ' + v

def my(x = 3, y = 3):
    return x ** y


def ff():
    try:
        print('begin', end=" ")
        return "result"
        print("end", end= " ")
    finally:
        print("final", end= " ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    l = [1,2]
    l1 = [3,2]

    print(zip(l, l1))
    print(all([[[]]]))






    print(os.listdir())

    print(ff())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
