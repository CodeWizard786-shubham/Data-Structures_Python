'''
@Author: shubham shirke
@Date: 2023-06-08 14:48:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 14:48:30
@Title : Python program to sum all the items in a list
'''

def sum_of_elements(number):
    """
    Description : 
            This function stores element in the list and find the sum of elements by adding one by one element from the list.
    Parameters : 
            number : specifies number of elements to store in list.
    Return     :
            sum : sum of all elements from list.
    
    """
    list = []
    sum = 0
    for _ in range(number):
        element =int(input("Enter element: "))
        list.append(element)
    
    # iterate over the list to add the elemnts to sum.
    for i in list:
        sum += i

    return sum
    

# main
def main():
    number = int(input("Enter size of list: "))
    sum = sum_of_elements(number)
    print(f"The sum of elements from the list is: {sum}")


if __name__ == "__main__":
    main()