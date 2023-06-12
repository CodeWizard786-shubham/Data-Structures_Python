'''
@Author: shubham shirke
@Date: 2023-06-09 19:50:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 19:50:30
@Title : Python program to remove duplicates from a list of lists
'''


def remove_dublicates_list(list1):
    """
    Description : 
            This function only stores list of list which are not present in unique_list.
    Parameters :
            list : list 1 with input elements.
    Returns : 
            unique_list : unique list of elemtents.
    """
    unique_lists = []
    for sublist in list1:  # sublist are the list in list
        if sublist not in unique_lists:
            unique_lists.append(sublist)
    
    return unique_lists


# main
def main():
    list_elements = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    result = remove_dublicates_list(list_elements)
    print(f"The new list is: {result}")


if __name__ == "__main__":
    main()