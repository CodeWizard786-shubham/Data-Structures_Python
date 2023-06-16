'''
@Author: shubham shirke
@Date: 2023-06-08 10:45:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 10:45:30
@Title : Python program to lowercase first n characters in a string.
'''

def lowercase_charaters(text,num):
        """
        Description : 
                This function finds the first N char from string and replace them to lower case.
        Parameters :
                text : input string from user
                num : number of character from string to change to lower case.
        Return  : 
                returns nonthing
                prints new string
        """
        first = text[:num]
        new_string = first.lower() + text[num:]    #  string slicing
        print(new_string)

# main
def main():
    text = input("Enter string: ")
    number_of_char = int(input("Enter number of characters to change: "))
    lowercase_charaters(text,number_of_char)


if __name__ == "__main__":
    main()