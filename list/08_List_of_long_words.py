'''
@Author: shubham shirke
@Date: 2023-06-09 15:10:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 15:10:30
@Title :   Python program to find the list of words that are longer than n from a given list of words.
'''

def get_list_of_long_words(elements_of_list,number):
    """
    Description : 
            This function stores elements in the list and prints the elements that are greater than number by user.
    Parameters :
            elements_of_list : string input from the user.
            number : length of the words to be greater than.
    Return  :
            none
            prints elements.
    """
    elements = elements_of_list.split(" ")
    list_of_words = []
    for ele in elements:
        list_of_words.append(ele)
    
    for ele in list_of_words:
        if(len(ele) > number):
            print(f"The elements are: {ele}")

def main():
    elements_of_list = input("Enter elemetents for list: ")
    number = int(input("Enter number to find longer words: "))
    get_list_of_long_words(elements_of_list,number)

if __name__ == "__main__":
    main()
