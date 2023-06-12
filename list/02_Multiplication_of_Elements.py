'''
@Author: shubham shirke
@Date: 2023-06-08 15:10:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 15:10:30
@Title : Python program to multiplies all the items in a list.
'''

def mul_of_elements(number):
    """
    Description : 
            This function stores element in the list and find the multiplication of elements by multiplying one by one element from the list.
    Parameters : 
            number : specifies number of elements to store in list.
    Return     :
            mul : multiplication of all elements from list.
    
    """
    list = []
    mul = 1
    for _ in range(number):
        element =int(input("Enter element: "))
        list.append(element)
    
    # iterate over the list to add the elemnts to sum.
    for i in list:
        mul = mul*i

    return mul
    

# main
def main():
    number = int(input("Enter size of list: "))
    mul = mul_of_elements(number)
    print(f"The multiplication of elements from the list is: {mul}")


if __name__ == "__main__":
    main()