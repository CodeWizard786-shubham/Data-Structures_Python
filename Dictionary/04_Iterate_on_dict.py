'''
@Author: shubham shirke
@Date: 2023-06-10 14:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 14:35:30
@Title :  Python program to iterate over dictionaries using for loops.
'''

def get_dictionary_items(dict_elements):
    """
    Descripition : 
            This function iterates over the dictionary items for key and value.
    Paremeters  :
            dict_elements : contains dict of elements.
    Retruns    :
            none
            print key and value for each item in dictionary
    """
    for key , value in dict_elements.items():
  
        print(f" key:{key} : value:{value}")


# main
def main():
    dict_elements = {0:1,1:2,2:3,3:4,4:5}
    get_dictionary_items(dict_elements)



if __name__ == "__main__":
    main()


