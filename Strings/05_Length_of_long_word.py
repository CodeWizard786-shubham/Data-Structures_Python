'''
@Author: shubham shirke
@Date: 2023-06-07 22:13:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 22:13:30
@Title : Python program that takes a list of words and returns the length of the longest one.
'''

def length_of_longest_word(num):
    """
    Description : 
            This function stores a list of words and then checks the length of words, 
            if any word has length greater than previous word store and print it.
    Paramenters : 
            num - number of words to take as input.
    Result : 
            Print length of the longest word.

    """
    # stroring words in list
    list=[]
    for number in range(1,num+1):
        word = input(f"Enter word {number}: ")
        list.append(word)

    # finding longest word in list with its length 
    longest_length = 0
    for word in list:
        if len(word) > longest_length:
            longest_length = len(word)
    print(f"The length of the longest word is: {longest_length}")

# main
def main():
    num = int(input("Enter number of words: "))
    length_of_longest_word(num)

if __name__ == "__main__":
    main()


