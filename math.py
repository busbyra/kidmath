#!/usr/bin/python3
'''
Main math file that asks the user to choose decimal, regular or quit.

'''
import random
import decimal as de
import multiplication as mu


def func():
    '''
    This function operates as the 'main' function to determine what the user
    wants to do and then executes it.
    '''
    response = 0
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

