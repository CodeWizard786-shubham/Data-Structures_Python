'''
@Author: shubham shirke
@Date: 2023-06-09 18:44:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 18:44:30
@Title : Python program to find common items from two lists.
'''

def common_in_lists(list1 ,list2):
    """
    Description : 
            This function checks if any element from list1 is present in list2. if found store it in comman_elements_list.
    Parameters :
            list1 : list 1 with user input elements
            list2 : list 2 with user input elements
    Returns : 
            common_elements_list : list containing elements if are found in both the lists.
    """
    common_elements_list = []
    for ele_1 in list1:
        for ele_2 in list2:
            if ele_1 == ele_2:
                common_elements_list.append(ele_1)
    return common_elements_list

# main
def main():
    list_elements_1 = list(map(str, input("Enter elements separated by spaces: ").split())) 
    list_elements_2 = list(map(str, input("Enter elements separated by spaces: ").split())) 
    common_elements = common_in_lists(list_elements_1,list_elements_2)
    print(f"Common elements from both the list are: {common_elements}")


if __name__ == "__main__":
    main()