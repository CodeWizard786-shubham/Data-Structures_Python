'''
@Author: shubham shirke
@Date: 2023-06-09 15:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 15:25:30
@Title : Python function that takes two lists and returns True if they have at least one common member.
'''

def compare_list(elements_for_list_1,elements_for_list_2):
    """
    Description : 
                This function stores input strings into two list using str.split function then compares both the list to check any comman elemtent found.
    Parameters : 
                elements_for_list_1 : input string for list_1
                elements_for_list_2 : input string for list_2
    Returns    :
                true or false
    """
    elements_1 = elements_for_list_1.split(" ")
    elements_2 = elements_for_list_2.split(" ")

    # create list 1
    list_1 = []
    for ele in elements_1:
        list_1.append(ele)
    
    # create list 2
    list_2 = []
    for ele in elements_2:
        list_2.append(ele)

    # compare list_1 and list_2:     
    for ele_1 in list_1:
        for ele_2 in list_2:
            if ele_1 == ele_2:
                return True
    return False

# main
def main():
    elements_for_list_1 = input("Enter elements for list 1: ") 
    elements_for_list_2 = input("Enter elements for list 2: ")
    output = compare_list(elements_for_list_1,elements_for_list_2)
    print(f"Output : {output}")


if __name__ == "__main__":
    main()