'''
@Author: shubham shirke
@Date: 2023-06-10 17:45:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 17:45:30
@Title : Python program to create a dictionary from a string and track the count of the letters from the string.
'''

def get_dictionary_items(string):
    """
    Descripition : 
            This function iterates over string and checks if any char is present in dict, if it does increase value by 1 or keep 1.
    Paremeters  :
            string : string input from user. 
    Retruns    :
            dict_elements : returns a dict containing char as key and count of occurance as values.
    """
    dict_elements = {}

    for char in string:
        if char in dict_elements:
            dict_elements[char] += 1
        else:
            dict_elements[char] = 1

    return dict_elements
    

    # main
def main():
    string = input("Enter a string: ")
    result_dict = get_dictionary_items(string)
    print(f"The result dictionary is: {result_dict}")



if __name__ == "__main__":
    main()









