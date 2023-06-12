'''
@Author: shubham shirke
@Date: 2023-06-07  21:59:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 21:59:30
@Title :  Python program to access environment variables.
'''

import os

def environment_variable(env_var):
    """
    Description : 
        This function access the environment variable.
    Parameters :
        none
    Return : 
            retruns nothing 
            prints result of the environment variable

    """
    if env_var in os.environ:
        variable_value = os.environ[env_var]
        print(variable_value)
    else :
        print("Environment variable does not exist")

# main
def main():
    env_var = 'PATH'
    environment_variable(env_var)


if __name__ == "__main__":
    main()