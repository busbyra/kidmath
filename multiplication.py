# Import stuff you need
import random


def func():
    print("Welcome to the multiplication game.")
    print("How well do you know your 2-12 multiplication tables?")
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
