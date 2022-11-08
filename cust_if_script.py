#!/usr/bin/env python3
"""A simple program using conditionals to make a decision"""


def main():

    score = int(input("Enter your mark "))
    if score >= 90:
        print(str(score) + "% " + "Well done, you achieved an A")

    elif score >= 80:
        print("Well done, you achieved a B")

    elif score >= 70:
        print("You achieved a C")

    elif score >= 60:
        print("You got a D")

    else:
        print("You're Expelled")


if __name__=="__main__":
    main()
   



