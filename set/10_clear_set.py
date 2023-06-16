'''
@Author: shubham shirke
@Date: 2023-06-10 12:50:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 12:50:30
@Title : Python program to clear a set.
'''

def clear_elements_in_set(set_of_elements):
    """
    Descripition : 
            This function returns a empty set from a given set.
    Paremeters  :
            set1 : contains set 1 of elements from user input.
    Retruns     :
            empty_set
    """
    set_of_elements.clear()

        
    return set_of_elements


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    result = clear_elements_in_set(set_of_elements_1)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


