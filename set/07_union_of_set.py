'''
@Author: shubham shirke
@Date: 2023-06-10 10:50:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 10:50:30
@Title : Python program to create a union of set.
'''

def get_elements_in_set(set_of_elements_1,set_of_elements_2):
    """
    Descripition : 
            This function finds elements that are present in both the sets excluding the repeated ones.
    Paremeters  :
            set_of_elements_1 : contains set 1 of elements.
            set_of_elements_2 : contains set 2 of elements.
    Retruns     :
            result set 
    """
    result_set = set_of_elements_1.union(set_of_elements_2)    # get all elements between two set's excluding the repeated ones.


    return result_set


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    set_of_elements_2 = set(input("Enter elements separated by spaces: ").split())
    result = get_elements_in_set(set_of_elements_1,set_of_elements_2)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


