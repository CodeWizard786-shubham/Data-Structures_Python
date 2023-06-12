'''
@Author: shubham shirke
@Date: 2023-06-07  14:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 14:15:30
@Title :  Python program to check file exist or not.
'''

import os

def check_file_existense(file_path):
    """
    Description : 
            This function checks if the file exist using the 'path.exists' function from 'os' module.
    Parameters : 
            file_path - URL path of the file.
    Result   :
          prints file exist or not.
    """
    if os.path.exists(file_path):
        print("file exists")
    else:
        print("File doesn not exist")

# main
def main():
    file_path= 'C:\\Users\\Shubham\\OneDrive\\Documents\\Bridgelabs CFP Data Engineering\\python\\test.py'
    check_file_existense(file_path)


if __name__ == "__main__":
    main()