'''
@Author: shubham shirke
@Date: 2023-06-10 13:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 13:35:30
@Title : Python script to add a key to a dictionary.
'''

def add_to_dictionary(dict_elements,key,value):
    """
    Descripition : 
            This function adds a key and value input from user to original dictionary.
    Paremeters  :
            dict_elements : contains dict of elements.
            key : key from user.
            value : value from the user.
    Retruns    :
            dict_elements : updated dictionary.
    """
    
    dict_elements[key] = value    

    return dict_elements


# main
def main():
    dict_elements = {0:1,1:2,2:3}
    key_element = eval(input("Enter key: "))
    value_element = eval(input("Enter key: "))
    dict_elements = add_to_dictionary(dict_elements,key_element,value_element)
    print(f"The dictionary of elements is: {dict_elements}")



if __name__ == "__main__":
    main()


