'''
@Author: shubham shirke
@Date: 2023-06-08 09:13:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 09:13:30
@Title : Python program to get the last part of a string before a specified character.
'''

def modified_String(string):
    """
    Description : 
            This function splits the string by specified character and creates a tuple of string.
    Parameters :
            string - input string.
    Result : new_string before specfied character.
    """
    new_string = string.rsplit('-',1)[0]   # [0] prints the word at index 0 in tuple.
    print(new_string)

# main
def main():
    string = "https://www.w3resource.com/python-exercises"
    modified_String(string)

if __name__ == "__main__":
    main()




