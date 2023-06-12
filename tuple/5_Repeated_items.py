'''
@Author: shubham shirke
@Date: 2023-06-09 22:48:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 22:48:30
@Title : Python program to find the repeated items of a tuple.
'''


def get_repeated_items_in_tuple(list_elements):
    """
    Description : 
            This function iterates over the tuple and checks if the items in the tuple count is greater than 1 and items not in present in the list.
    Parameters : 
            list_elements : list of elements by user input.
    Returns : 
            list : list of repeated items.
    """
    list = []
    for items in list_elements:
        if list_elements.count(items) > 1 and items not in list:
            list.append(items)

    return list

# main
def main():
    list_elements = tuple(map(int, input("Enter elements separated by spaces: ").split()))
    repeated_items = get_repeated_items_in_tuple(list_elements)
    print(f"Repeated items in the tuple are: {tuple(repeated_items)} ")


if __name__ == "__main__":
    main()
