'''
@Author: shubham shirke
@Date: 2023-06-10 18:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 18:00:30
@Title : Python program to print a dictionary in table format.
'''

from tabulate import tabulate

def print_dictionary_in_table(string):
    """
    Description:
            This function converts the input string into a dictionary and prints it in a table format.
    Parameters:
            string : The string input from the user.
    Returns:
            table (list): A list of lists containing the key-value pairs.
    """
    string_elements = string.split()
    dict_elements = {}
    for item, word in enumerate(string_elements, start=1):
        dict_elements[item] = word

    table = []
    # get items from dict and store to table list
    for key,value in dict_elements.items():
        table.append([key, value])
    
    return table

    # main
def main():
    string = input("Enter a string elements with spaces: ")
    table = print_dictionary_in_table(string)
    print(tabulate(table, headers=["Key", "Value"], tablefmt="grid"))



if __name__ == "__main__":
    main()
