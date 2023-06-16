'''
@Author: shubham shirke
@Date: 2023-06-10 11:26:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 11:26:30
@Title : Python program to find symmetric difference in set.
'''

def get_elements_in_set(set1,set2):
    """
    Descripition : 
            This function returns a set containg elements which are either in set A or in set B but not in both
    Paremeters  :
            set1 : contains set 1 of elements from user input.
            set2 : contains set 2 of elements from user input
    Retruns     :
            symm_diff
    """
    sym_diff = set()

    for elem in set1:
        if elem not in set2:
            sym_diff.add(elem)

    for elem in set2:
        if elem not in set1:
            sym_diff.add(elem)
        
    return sym_diff


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    set_of_elements_2 = set(input("Enter elements separated by spaces: ").split())
    result = get_elements_in_set(set_of_elements_1,set_of_elements_2)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


