'''
@Author: shubham shirke
@Date: 2023-06-07  14:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 14:15:30
@Title :  Python program to check file exist or not.
'''

import os

def call_external_command(command):
    """
    Description : 
            This function executes given system commands.
    Parameters : 
            command : system command from user.
    Return : 
            returns nothing 
            result of system commands
    """
    os.system(command)


def main():
    command = input("Enter command: ")
    call_external_command(command)


if __name__ == "__main__":
    main()