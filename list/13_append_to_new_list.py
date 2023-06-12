'''
@Author: shubham shirke
@Date: 2023-06-09 18:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 18:20:30
@Title : Python program to append a list to the second list.
'''

def get_new_list(list_elements):
    """
    Description : 
                This function appends all the elements from list_elements to new_list.
    Parameters : 
            list_elemments : list containing user input elements.
    Returns :
            new_list
    """
    new_list = []
    if len(list_elements) > 0:
        for ele in list_elements:
            new_list.append(ele)

    return new_list


# main
def main():
    list_elements = list(map(int, input("Enter numbers separated by spaces: ").split()))    
    new_list = get_new_list(list_elements)
    print(f"The new list is: {new_list}")



if __name__ == "__main__":
    main()


