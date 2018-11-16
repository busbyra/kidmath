#!/usr/bin/python3
'''
decimal.py

The decimal function is used for multiplication of numbers from 0 thru 12 with
all decimal number out to the ten thousandth.


I broke these out into separate files instead of keeping them all in one
mostly "just because".
'''
import random


def func():
    '''
    Function should be called by another function to run.
    This function takes two numbers, multiplies, and stores them
    in an answer key.
    '''
    print("Welcome to the multiplication game.")
    print("How well do you know your 2-12 multiplication tables?")
    for num in range(0,10):
        #pick the numbers to multiply
        number1 = round(random.uniform(0,12), 4)
        number2 = round(random.uniform(0,12), 2)
        answer = round(number1 * number2, 4)
        guess = 0
        print("What is", number1, "x", number2, "?")
        while guess != answer:
            guess = input("Answer: ")
            
            if guess.lower() == 'q':
                # Could just put a return back to the main program.
                raise SystemExit
            try:
                int(guess)
                if float(guess) != answer:
                    print(answer)
                    print("No, try again")
                else:
                    print("You got it!")
                    break
            except:
                print("Not a valid response")

    print("That's it, good work!")


if __name__=="__main__":
    func()

