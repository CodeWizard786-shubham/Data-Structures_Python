'''
@Author: shubham shirke
@Date: 2023-06-08 10:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 10:25:30
@Title :  Python program to count occurrences of a substring in a string.
'''

def substring_of_string(text,sub_string):
    """
    Description : 
            This function check occurances of the substring from the string.
    Parameters :
            text - input string
            start_index - start index number 
            end_index - end index number
    Return : 
            returns nothing
            prints 
    """
    count = text.count(sub_string)
    print(f"The substring '{sub_string}' appears {count} times")

# main
def main():
    text = input("Enter a string: ")
    sub_string = (input("Enter substring to check for occurance: "))
    substring_of_string(text,sub_string)


if __name__ == "__main__":
    main()