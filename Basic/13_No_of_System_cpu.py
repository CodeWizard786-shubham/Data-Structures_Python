'''
@Author: shubham shirke
@Date: 2023-06-07  21:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 21:30:30
@Title :  Python program to print number of CPU's being used by the system.
'''

import os

def system_processor():
    """
    Description : 
            This function prints the number of cpu's system is using.
    Parameters : 
            none
    Return : 
            returns number of CPU
    """
    count=os.cpu_count()
    print(f"Ths number of CPU's being used by the system are: {count}")

# main
def main():
    system_processor()


if __name__ == "__main__":
    main()