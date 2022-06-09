#!/bin/python3

def welcome(name):
    """
    Say hi to ACB attendees
    """
    print(f'{name}, welcome to ACB 2022')


if __name__ == '__main__':
    names = ['Bob', 'Harry', 'Tom', 'Willis']
    for name in names:
        welcome(name)    

