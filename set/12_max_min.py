'''
@Author: shubham shirke
@Date: 2023-06-10 13:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 13:20:30
@Title : Python program to find max and min value in set.
'''

def get_max_min_in_set(set_of_elements):
    """
    Descripition : 
            This function returns maximim and minimum value from the set.
    Paremeters  :
            set_of_elements : contains set of elements from user input.
    Retruns     :
            max_value
            min_value
    """
    max_value = max(set_of_elements)    # max function to get maximum value from set
    min_value = min(set_of_elements)    # min function to get minimum value in the set

    return max_value , min_value


# main
def main():
    set_of_elements_1 = set(input("Enter elements separated by spaces: ").split())
    max_value , min_value = get_max_min_in_set(set_of_elements_1)
    print(f"The maximum value in set is: {max_value} and minimum value in set is: {min_value}")


if __name__ == "__main__":
    main()


