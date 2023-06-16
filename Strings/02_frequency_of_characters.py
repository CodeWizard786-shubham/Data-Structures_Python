'''
@Author: shubham shirke
@Date: 2023-06-07 20:55:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 20:55:30
@Title : Python program to find frequency of characters in string.
'''

def frequency_characters(string):
    """
    Description : 
            This function generates a dicionary containing frequency of characters where character is the key and frequency is value.
    Parameters :
            string - string input from the user
    Result : 
            dictionary with characters and frequency count.
    
    """
    string = string.replace(" ","")  #remove space from the string
    dict = {}
    for char in string:
        if char in dict:     # check if the char is already present in the dict.
            dict[char]+=1
        else:
            dict[char]=1
    print("Frequncy of characters in string are:")
    print(dict)


# main
def main():
    string = input("Enter string : ")
    frequency_characters(string)


if __name__ == "__main__":
    main()