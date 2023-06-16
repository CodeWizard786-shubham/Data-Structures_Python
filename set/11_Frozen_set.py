'''
@Author: shubham shirke
@Date: 2023-06-10 13:05:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 13:05:30
@Title : Python program to use of frozensets.
'''

def frozen_elements_in_set(set_of_elements):
    """
    Descripition : 
            This function returns a empty set from a given set.
    Paremeters  :
            set1 : contains set 1 of elements from user input.
    Retruns     :
            empty_set
    """
    new_frozen_set = frozenset(set_of_elements)  # frozen sets are immutable sets.


    return new_frozen_set


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    result = frozen_elements_in_set(set_of_elements_1)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


