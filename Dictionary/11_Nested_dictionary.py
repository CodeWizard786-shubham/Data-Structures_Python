'''
@Author: shubham shirke
@Date: 2023-06-10 19:05:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 19:05:30
@Title : Python program to convert a list into a nested dictionary of keys.
'''

def list_to_nested_dictionary(keys_list, value):
    """
    Descriptio :
            This function creates a nested dictionary of keys.
    Parameters :
            keys_list : list of keys,
            value : value for key.
    Returns : 
            nested_dict
    """
    nested_dict = {}
    current_dict = nested_dict

    for key in keys_list[:-1]:
        current_dict[key] = {}
        current_dict = current_dict[key]

    current_dict[keys_list[-1]] = value

    return nested_dict


# main
def main():
    keys_list = ['a', 'b', 'c']
    value = 10
    nested_dict = list_to_nested_dictionary(keys_list, value)
    print(nested_dict)


if __name__ == "__main__":
    main()








