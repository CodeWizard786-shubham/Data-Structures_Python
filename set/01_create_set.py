'''
@Author: shubham shirke
@Date: 2023-06-10 10:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 10:15:30
@Title : Python program to create a set.
'''


def create_set(set_of_elements):
    """
    Descripition : 
            This function returns a set of elements given as input enclosed in curly braces.
    Paremeters  :
            set_of_elements : contains set of elements.
    Retruns     :
            set_of_elements
    """
    return set_of_elements

# main
def main():
    set_of_elements = set(map(int, input("Enter elements separated by spaces: ").split()))
    result = create_set(set_of_elements)
    print(f"The result set is: {result}")


if __name__ == "__main__":
    main()