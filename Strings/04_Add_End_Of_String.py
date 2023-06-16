'''
@Author: shubham shirke
@Date: 2023-06-07 21:50:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 21:50:30
@Title : Python program to add 'ing' at the end of a given string (length should be at least 3. 
        If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
'''

def add_end_of_string(string):
    """
    Description : 
            This function checks if the last three characters are 'ing', if it does replace with 'ly' otherwise add 'ing' at the end.
    Parameters :
            string : input string from the user.
    Return :
            returns nothing
            prints new string with changes.
    
    """
    if(len(string)>=3):
        if string[-1] == 'g' and string[-2] == 'n' and string[-3] == 'i':
            string += 'ly' 
            print(f"The result of the string with 'ly' is: {string}")
        else:
            string += 'ing'
            print(f"The result of the string with 'ing' is: {string}")

# main
def main():
    string = input("Enter string: ")
    add_end_of_string(string)


if __name__ == "__main__":
    main()