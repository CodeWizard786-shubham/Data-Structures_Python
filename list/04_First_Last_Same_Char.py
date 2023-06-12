'''
@Author: shubham shirke
@Date: 2023-06-09 13:24:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 13:21:30
@Title : Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of string.
'''

def count_same_string(string):
    """
    Description : This function stores the element in the list and check if the length of the element is greater than do. 
                    if condition satisfied checks if the first and last char is same and increase the count.
    Parameters : 
            string : string input from the user.
    Return  :
            count - count of elements from the list having first and last character same.
    """
    list=[]
    string_1 = string.split(" ")
    # storing elemments in list
    for ele in string_1:
        list.append(ele)

    count = 0
    # check the condition and increase the count if satisfied.
    for ele in list:
        if (len(ele) >= 2):
            if(ele[0] == ele[-1]):
                count +=1
    return count

# main
def main():
    string=input("Enter string: ")
    count = count_same_string(string)
    print(f"The count for first and last element being same is: {count} ")


if __name__ == "__main__":
    main()