'''
@Author: shubham shirke
@Date: 2023-06-10 11:05:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 11:05:30
@Title : Python program to create set difference.
'''

def get_elements_in_set(set_of_elements_1,set_of_elements_2):
    """
    Descripition : 
            This function returns a set containg elements that are present in set 1 and not in set 2.
    Paremeters  :
            set_of_elements_1 : contains set 1 of elements from user input.
            set_of_elements_2 : contains set 2 of elements from user input
    Retruns     :
            result_set
    """
    result_set = set_of_elements_1.difference(set_of_elements_2)    # get elements which are present in set 1 but not in set two.


    return result_set


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    set_of_elements_2 = set(input("Enter elements separated by spaces: ").split())
    result = get_elements_in_set(set_of_elements_1,set_of_elements_2)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()


