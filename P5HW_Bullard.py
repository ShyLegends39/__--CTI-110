# A brief description of the project: This program uses loops and functions and
# module import to process and calculate the data to be made into a simple math quiz!

# November 26, 2022

# CTI-110 P5HW - Math Quiz

# Kelly Bullard

#

import random


def addProblem():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f'  {a}')
    print(f'+ {b}\n')
    print('Enter answer.')
    ans = int(input())
    numGuess = 0
    
    while ans!= (a+b):
        numGuess+=1
        if ans < (a+b):print('Sorry, guess is too low.\n')
        else: print('Sorry, guess is too high.\n')
        ans = int(input('try again: '))
    print('Congratulations!!!! your answer is correct...')
    print(f'Number of guesses: {numGuess+1}') #  numGuess+1 is including the answer input by add 1 to it.
                                              #  EX: If you are right the first time without getting any try again then you get just 1 for the Number of guesses that you guess/answer!
    print('') # space

def subProblem():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if a<b:a,b=b,a
    print(f'  {a}')
    print(f'- {b}\n')
    print('Enter answer.')
    ans = int(input())
    numGuess = 0
    
    while ans!= (a-b):
        numGuess+=1
        if ans < (a-b):
            print('Sorry, guess is too low.\n')
        else:
            print('Sorry, guess is too high.\n')
        ans = int(input('try again: '))
    print('Congratulations!!!! your answer is correct...')
    print(f'Number of guesses: {numGuess+1}') #  numGuess+1 is including the answer input by add 1 to it.
                                              #  EX: If you are right the first time without getting any try again then you get just 1 for the Number of guesses that you guess/answer!
    print('') # space

def main():
    print('Welcome to Math Quiz\n')
    print('') # space
    while True:
        print('MAIN MENU')
        print('--------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addProblem()
        elif choice == '2':
            subProblem()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break


main()
