'''
@Author: shubham shirke
@Date: 2023-06-07 21:26:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 21:26:30
@Title : Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
'''

def replace_char_in_string(string):
    """
    Description : 
            This function prints the $ symbol for all the occurances of first character again in string.
    Parameters : 
            string - string input from the user.
    Result : 
            new_string or else print no occurance of first char found.
    """
    first_char = string[0]
    if first_char in string[1:]:      # check if the first char occur again in the string
        new_string = first_char + string[1:].replace(first_char, '$')
        print(new_string)
    else:
        print("There is no another occurance of first character")

# main  
def main():
    string = input("Enter string: ")
    replace_char_in_string(string)


if __name__ == "__main__":
    main()