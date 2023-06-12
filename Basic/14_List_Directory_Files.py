'''
@Author: shubham shirke
@Date: 2023-06-07  21:45:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 21:45:30
@Title :  Python program to list all the files in given directory.
'''

import os

def list_directory_files(path):
    """
    Description : 
            This function list files from the directory.
    Parameters : 
            path - path of the directory
    Result : 
         Print list of file present in the directory.
    """
    if os.path.exists(path):
        directroy_filess=os.listdir(path)
        print(directroy_filess)
    else :
        print("Path not found")

def main():
    path = "C:\\Users\\Shubham\\OneDrive\\Documents\\Bridgelabs CFP Data Engineering\\python"
    list_directory_files(path)


if __name__ == "__main__":
    main()