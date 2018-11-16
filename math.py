import random
import decimal as de
import multiplication as mu


def func():
    response = 1
    while(response != 'q'):
        print("All right, Kainan!  Let's do some math!")
        print("Select which sort of math you would like to work on.")
        print("1.) Decimal Multiplication")
        print("2.) Regular Multiplication")
        print("Or Press Q to exit")

        response = input(">>> ")    
        print(response)

        if response == '1':
            print('rip')
            de.func()
        if response == '2':
            mu.func()
        if response == 'q':
            raise SystemExit

    


if __name__=="__main__":
    func()

