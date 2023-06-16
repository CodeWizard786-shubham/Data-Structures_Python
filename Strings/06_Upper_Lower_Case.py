'''
@Author: shubham shirke
@Date: 2023-06-07 22:40:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 22:40:30
@Title : Python program that takes a list of words and returns the length of the longest one.
'''

def upper_lower_case(string):
    """
    Description : 
            This function converts given string to upper case and lower case.
    Parameters : 
            string - string inout from the user
    Result : 
            upper_case_string 
            lower_case_string
    """
    # conversion using uppercase and lower case fucntion.
    upper_case_string = string.upper()
    lower_case_string = string.lower()

    # Print result
    print(f"The string in upper case : {upper_case_string}")
    print(f"The string in lower case : {lower_case_string}")

# main
def main():
    string=input("Enter string: ")
    upper_lower_case(string)

if __name__ == "__main__":
    main()