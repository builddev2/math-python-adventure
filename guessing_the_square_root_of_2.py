from bdb import Breakpoint
import math
from passcode_for_guessing_the_square_root_of_2 import passcode2026618
print("Time to guess.")
firstabby = int(input("Give an estimate for x. It is around 1.4. You have 5 guesses. x**2(x to the power of 2) - 2 = 0(return goal). 1st guess: "))
xguess1 = firstabby**2 - 2
print("Return1:", xguess1)
secondabby = int(input("Guess 2: "))
xguess2 = secondabby**2 - 2
print("Return2:", xguess2)
thirdabby = int(input("Guess 3: "))
xguess3 = thirdabby**2 - 2
print("Return3:", xguess3)
fourthabby = int(input("Guess 4: "))
xguess4 = fourthabby**2 - 2
print("Return4:", xguess4)
fifthabby = int(input("Guess 5: "))
xguess5 = fifthabby**2 - 2
print("Return5:", xguess5)
reveal = input("Do you want to reveal the real answer(15 digits!)? ")
if reveal == "Yes"or "yes":
    passcodetest = int(input("What is the passcode(1 try)?"))
    if passcodetest == passcode2026618:
        print("................................" * 50)
        print("The square root of 2 is...")
        print("................................" * 30)
        print("...")
        print("................................" * 10)
        print("It is...   ", math.sqrt(2), "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("Wrong passcode. Wrong passcode. Stopping.")
        Breakpoint
elif reveal is not "yes" or "Yes" or "no" or "No":
    print("Looks like a maybe.")
    passcodetest2 = int(input("What is the passcode(1 try)? "))
    if passcodetest2 == passcode2026618:
        answer = input("Yes or No? ")
        if answer == "Yes":
            print("................................" * 50)
            print("The square root of 2 is...")
            print("................................" * 30)
            print("...")
            print("................................" * 10)
            print("It is...   ", math.sqrt(2), "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("Ok.")
            Breakpoint
    else:
        print("Wrong passcode. Wrong passcode. Stopping.")
        Breakpoint
else:
    print("Looks like a no.")
    Breakpoint

