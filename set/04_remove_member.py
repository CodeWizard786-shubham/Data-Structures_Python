'''
@Author: shubham shirke
@Date: 2023-06-10 10:27:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 10:27:30
@Title : Python program to remove a members in the set.
'''

def get_elements_in_set(set_of_elements,element):
    """
    Descripition : 
            This function removes an element given as a input by user to a set using set.remove().
    Paremeters  :
            set_of_elements : contains set of elements.
            element : value to add in the set.
    Retruns     :
            set_of_elements.
    """
    set_of_elements.remove(element)


    return set_of_elements


# main
def main():
    set_of_elements = set(input("Enter elements separated by spaces: ").split())
    element_to_add = eval(input("Enter element to add in the set: "))
    result = get_elements_in_set(set_of_elements,element_to_add)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


