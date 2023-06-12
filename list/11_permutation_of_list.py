'''
@Author: shubham shirke
@Date: 2023-06-09 17:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 17:25:30
@Title : Python program to generate all permutations of a list in Python.
'''

from itertools import permutations

def get_permutations(element_list):
    """
    Description : 
            This function uses permutation module to perform the permutation on input list.
    Parameters : 
            element_list : elements for list input from user.
    Return      :
            permutation_list
    """
    permutation_list = []
    sub_strings = permutations(element_list)
    # iterate over the permute sub_string to store in permutation_list.
    for ele in sub_strings:
        permutation_list.append(ele)
    
    return permutation_list

# main
def main():
    string_element =input("Enter string of elements: ")
    elements_list = string_element.split()
    permutation_list= get_permutations(elements_list)
    print(f"The permutation list is : \n {permutation_list}")


if __name__ == "__main__":
    main()