'''
@Author: shubham shirke
@Date: 2023-06-08 15:21:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 15:21:30
@Title : Python program to smallest number from the list.
'''

def smallest_in_list(list_size):
    """
    Description : 
            This function stores elemetns in the list and sort the list to get smallest element.
    Parameter : 
            list_size : size of the list.
    Return :
            none
            print sorted list and smallest number.
    """
    # store elements in list
    list = []
    for _ in range(list_size):
        element =int(input("Enter element: "))
        list.append(element)

    temp = 0
    for i in range(len(list)):     # bubble sort algo logic to sort the elements in list.
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            i+=1
            j+=1

    smallest_number = list[0]
    print(f"The list is :{list}")
    print(f"The smallest number in the list is : {smallest_number}")

# main
def main():
    list_size =int(input("Enter the sixe of the list: "))
    smallest_in_list(list_size)


if __name__ ==  "__main__":
    main()