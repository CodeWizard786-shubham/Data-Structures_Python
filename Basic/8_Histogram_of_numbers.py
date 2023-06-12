'''
@Author: shubham shirke
@Date: 2023-06-07  01:34:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 01:34:30
@Title : Python program to print histogram (Pattern) from the given list of integers.
'''

def histogram_of_numbers(num):
    """
    Description : 
            This function stores numbers in a list and prints * symbol as per numbers in list.
    Parameters : 
           num - this value depicts the number of integers to store in list.
    Result :
            histogram pattern of * symbol.
    """
    list=[]
    #store numbers in list
    for i in range(1,num+1):
        number = int(input(f"Enter numbers {i}: "))
        list.append(number)
    
    # print in histogram pattern
    for num in list:
        print('*' * num)

# main
def main():
    num = int(input("Enter number of inputs: "))
    histogram_of_numbers(num)


if __name__ == "__main__":
    main()