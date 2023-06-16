'''
@Author: shubham shirke
@Date: 2023-06-10 10:27:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 10:27:30
@Title : Python program to iterate over set.
'''

def get_elements_in_set(set_of_elements):
    """
    Descripition : 
            This function iterates over the set and prints the elements from  the set.
    Paremeters  :
            set_of_elements : contains set of elements.
    Retruns     :
            none  : prints each item in set.
    """
    for item in set_of_elements:
       print(item,end=" ")    # end operater to print items in single line.


# main
def main():
    set_of_elements = set(map(int, input("Enter elements separated by spaces: ").split()))
    get_elements_in_set(set_of_elements)


if __name__ == "__main__":
    main()


