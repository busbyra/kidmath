#!/usr/bin/python3
'''
multiplication.py

This operates as the multiplication portion.
I could easily throw all of this into one file or at least add the decimal
portion to this in order to have it run all together, but I didn't.  Mostly
simply because I didn't want to.
'''
import random


def func():
    '''
    Randomly selects a pair of numbers and multiplies them.
    I set the initial guess value to -1.
    '''
    print("Welcome to the multiplication game.")
    print("How well do you know your multiplication table?")
    print("If you want to quit early, press Q\n")

    for num in range(0,10):
        #pick the numbers to multiply
        number1 = random.randint(0,12)
        number2 = random.randint(0,12)
        answer = number1 * number2
        guess = -1

        print("What is", number1, "x", number2, "?")
        while guess != answer:
            guess = input("Answer: ")
            if guess.lower() == 'q':
                raise SystemExit
        
            try:
                int(guess)    
                if int(guess) != answer:
                    print("No, try again")
                else:
                    print("You got it!")
                    break
            except:
                print("Not a valid response")
    
    print("That's it, good work!")


if __name__=="__main__":
    func()
