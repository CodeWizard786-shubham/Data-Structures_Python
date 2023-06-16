'''
@Author: shubham shirke
@Date: 2023-06-10 15:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 15:00:30
@Title : Python script to reove key from a dictionary.
'''

def get_dictionary_items(dict_elements,number):
    """
    Descripition : 
            This function removes key from the dictionary along with its value using pop function.
    Paremeters  :
            number : key to remove from dictionary. 
    Retruns    :
            dict_elements  : dictionary with updated form.
    """

    dict_elements.pop(number)

    return dict_elements


# main
def main():
    dict_elements = {1:'one',2:'two',3:'three',4:'four'}
    number = eval(input("Enter key to remove: "))
    new_dict = get_dictionary_items(dict_elements,number)
    print(f"The result dictionary is: {new_dict}")



if __name__ == "__main__":
    main()


