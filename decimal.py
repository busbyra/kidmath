import random

#print your welcome message here
def func():
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
                raise SystemExit

            if float(guess) != answer:
                print(answer)
                print("No, try again")
            else:
                print("You got it!")
                break
    print("That's it, good work!")

if __name__=="__main__":
    func()

