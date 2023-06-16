'''
@Author: shubham shirke
@Date: 2023-06-08 10:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 10:35:30
@Title : Python program to reverse a string.
'''

def string_reverse(text):
    """
    Description : 
            This function reversed the string by using string slicing.
    Parameters:
            text : input string from user.
    Return : 
            retruns nothing
            prints reverse_string
    """
    reverse_string = text[::-1]
    print(reverse_string)

# main
def main():
    text = input("Enter string to reverse: ")
    string_reverse(text)


if __name__ == "__main__":
    main()