'''
@Author: shubham shirke
@Date: 2023-06-10 10:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 10:35:30
@Title : Python program to create a intersection of set.
'''

def get_elements_in_set(set_of_elements_1,set_of_elements_2):
    """
    Descripition : 
            This function removes an element given as a input by user if it is present in the set or returns false.
    Paremeters  :
            set_of_elements : contains set of elements.
            element : value to add in the set.
    Retruns     :
            result_set.
    """
    result_set = set_of_elements_1.intersection(set_of_elements_2)    # get common elements between two sets.


    return result_set


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    set_of_elements_2 = set(input("Enter elements separated by spaces: ").split())
    result = get_elements_in_set(set_of_elements_1,set_of_elements_2)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


