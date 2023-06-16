'''
@Author: shubham shirke
@Date: 2023-06-10 19:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 19:30:30
@Title : Python program to count number of items in a dictionary value that is a list.
'''

def count_items_in_list_values(dict_elements):
    """
    Description : 
            This function counts the number of values present as list in the dictionary.
    Parameters :
            dict_elements : dictionary of elements containg some list as values.
    Returns :
            count - count of values in the list.
    """
    count = 0
    for value in dict_elements.values():
        if isinstance(value, list):
            count += len(value)
    return count

# main
def main():
    dict_elements = {'key1': [1, 2, 3], 'key2': 'value', 'key3': [4, 5, 6, 7]}
    result_count = count_items_in_list_values(dict_elements)
    print(f"Total items in list values: {result_count}")


if __name__ == "__main__":
    main()








