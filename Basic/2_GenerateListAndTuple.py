'''
@Author: shubham shirke
@Date: 2023-06-06  21:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-06 21:20:30
@Title : Python program to take numbers seperated by commas as input ans print them in list and tuple format.
'''


def generate_list_and_tuple(number_of_inputs): 
    """
    Description : This function takes in numbers of str type as input and generates a list and a tuple.
    Parameters :
        number_of_inputs : This value specifies how many numbers of take input.

    Result     :  list and tuple of numbers of data type string.
    """
    list = []
    for num in range(1,number_of_inputs+1):
        number = str(input(f"Enter number {num}: "))
        list.append(number)

    tuple_of_numbers=tuple(list)
    # print list and tuple
    print(f"List:{list}")
    print(f"Tuple:{tuple_of_numbers}")


# main function
def main():
    number_of_inputs =int(input("Enter how many number to take input: "))
    generate_list_and_tuple(number_of_inputs)


if __name__ == "__main__":
    main()