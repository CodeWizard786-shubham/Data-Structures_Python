'''
@Author: shubham shirke
@Date: 2023-06-08 09:13:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 09:13:30
@Title :  Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
'''

def sorted_words(string):
    """
    Description : 
            This function splits the given string by comas and store them in sort_list then used sorted function to sort the list.
    Parameters : 
            colors - comma seperated string
    Return : 
            returns nothing
            sorted_list - alphabetically
    """
    string_sort_list = string.split(',')
    sorted_list = sorted(set(string_sort_list))   # sorted function to arrange colors alphabetically
    print(sorted_list)

# main          
def main():
    string = input("Enter string (comma separated): ")
    sorted_words(string)


if __name__ == "__main__":
    main()