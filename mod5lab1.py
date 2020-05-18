"""
CTEC 121
Edward Lamanna
mod5 lab 1
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main1():
    print()
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")
    print()


# remove obvious dups
""" IPO happy()
Input(s): none
Process: prints/outputs chorus of happy birthday song
Output: prints to terminal screen
"""


def happy():
    print("Happy birthday to you!")


def main2():
    print()
    happy()
    happy()
    print("Happy birthday to you!")
    happy()
    print()


# generALIZE FOR ANY PERSON
""" IPO happy()
Input(s): name
Process: prints/outputs verse line of happy birthday song
Output: prints to terminal screen
"""


def happyBDay(name):
    print("happy birthday, dear ", name, "...", sep="")


def main3():
    print()
    happy()
    happy()
    happyBDay("Joe mama")
    happy()
    print()

# combine song into a function


""" IPO happy()
Input(s): name
Process: prints/outputs of happy birthday song
Output: prints to terminal screen
"""


def singhappyBday(name):
    happy()
    happy()
    happyBDay(name)
    happy()
    print()


def main4():
    print()
    singhappyBday("fred")
    singhappyBday("lucy")
    singhappyBday("bill")


main4()
