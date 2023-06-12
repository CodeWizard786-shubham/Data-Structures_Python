'''
@Author: shubham shirke
@Date: 2023-06-08 13:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 13:30:30
@Title : Python program to get the number of occurrences of a specified element in an array.
'''

from array import *

def occurance_in_array():
    array_1 = array('i',[1,2,3,4,1,3,4,5,1])
    count = 0
    spec_word = 1
    for word in array_1:
        if word == spec_word:
            count +=1
    return spec_word,count

def main():

    spec_word,count = occurance_in_array()
    print(f"The word {spec_word} occurs {count} times")

if __name__ == "__main__":
    main()