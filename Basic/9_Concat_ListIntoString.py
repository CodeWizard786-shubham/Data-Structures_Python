'''
@Author: shubham shirke
@Date: 2023-06-07  13:53:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 13:53:30
@Title : Python program to concatenate all elements in a list into a string and return it.
'''

def concat_list_to_string():
    """
    Description : 
            This function concatenate all elements in a list into a string and print it.
    Parameters :
            none
    Result : sentence contains concatenation of list elements.
    """

    list = ['I','am','learing','Python','for','Data','Engineering']
    sentence = " "
    for word in list:
        sentence += word + " "  # storing word as well as space in senetence varaible.
    print(type(sentence))
    print(sentence)
 
# main
def main():
    concat_list_to_string()


if __name__ == "__main__":
    main()