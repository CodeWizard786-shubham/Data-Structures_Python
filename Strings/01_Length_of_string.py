'''
@Author: shubham shirke
@Date: 2023-06-07 20:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 20:35:30
@Title : Python program to find the length of the string without spaces.
'''


def length_of_string(string):
    """
    Description : 
            This function removes spaces from the string and prints the length of string.
    Parameters : 
            string - input string from the user.
    Result : 
            length of the string in int.
    """
    string = string.replace(" ","")   # To store string without spaces
    length_of_string = len(string)
    print(f"The length of the string is: {length_of_string}")


# main
def main():
    string = input("Enter string: ")
    length_of_string(string)


if __name__ == "__main__":
    main()