'''
@Author: shubham shirke
@Date: 2023-06-09 18:25:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 18:25:30
@Title : python program to check whether two lists are circularly identical.
'''

def check_circular_identical(list1, list2):
    """
    Description : This function checks if the two given list are same. If true , double list 1 and conver to string format along with list 2.
                    Then checks if the string 2 is present in string 1. 
    Parameters: 
            list1 : user input list 1
            list 2 : user input list 2
    Returns  :
            returns boolean value
    """
    # Check if both lists have the same length
    if len(list1) != len(list2):
        return False

    # Create a string representation of list1 and list2
    list1_str = ' '.join(map(str, list1*2))   # concetenating list1 with itself.

    list2_str = ' '.join(map(str,list2))

    # Check if list2 is a substring of list1_str
    if list2_str in list1_str:
        return True

    return False


# main
def main():
    list_elements_1 = list(map(int, input("Enter numbers separated by spaces: ").split())) 
    list_elements_2 = list(map(int, input("Enter numbers separated by spaces: ").split()))    
    output = check_circular_identical(list_elements_1,list_elements_2)
    print(f"output: {output}")



if __name__ == "__main__":
    main()


