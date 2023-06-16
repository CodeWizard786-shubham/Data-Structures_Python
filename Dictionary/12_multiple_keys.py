'''
@Author: shubham shirke
@Date: 2023-06-10 19:05:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 19:05:30
@Title : Python program to check multiple keys exists in a dictionary.
'''

def check_multiple_keys(dict_elements,keys):
    """
    Descriptio :
            This function checks if the keys are present in the dictionary or not.
    Parameters :
            dict_elements : dictionary of elements from input.
            keys : key list.
    Returns : 
            nested_dict
    """
    for key in keys:
        if key not in dict_elements:
            return False
    return True

# main
def main():
    dict_elements = {1:'one',2:'two',3:'three',4:'four'} 
    keys_to_find = [1,2]
    result = check_multiple_keys(dict_elements, keys_to_find)
    if result == True:
        print("keys exist in the dictionary.")
    else:
        print("keys are missing from the dictionary.")


if __name__ == "__main__":
    main()








