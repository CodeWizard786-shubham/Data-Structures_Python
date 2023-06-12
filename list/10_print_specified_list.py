'''
@Author: shubham shirke
@Date: 2023-06-09 15:50:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 15:50:30
@Title : Python program to print a specified list after removing the 0th, 4th and 5th elements.
'''

def get_specified_list(string_element):
    """
    Description : 
            This function creates a list and deletes elements from the list as per index number.
    Parameters : 
            string_elements: user input string of elements.
    Returns :
            list : list with deleted elements at the specifies index number.
    """
    element = string_element.split(" ")
    # create a list
    list = []
    for ele in element:
        list.append(ele)
    
    # del function to delete elements in the list. 
    del list[5]
    del list[4]
    del list[0]

    return list

# main
def main():
    string_element = input("Enter string of elements: ")
    list = get_specified_list(string_element)
    print(f"The output list is: {list}")


if __name__ == "__main__":
    main()