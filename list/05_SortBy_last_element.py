'''
@Author: shubham shirke
@Date: 2023-06-09 13:43:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 13:21:30
@Title :  Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
'''

def last(n): 
    """
    Description : This function returns n with last index.
    Parameters : 
            n : tuples in list
    Retrun : 
            n[-1] : last element
    """
    return n[-1]

def get_sorted_list(tuple_list):
    """
    Description : 
            This function sorts the list containing tuples using sorted function.
    Parameters : 
            tuple_list : input list to sort
    Return  :
         sorted tuple_list
    """
    return sorted(tuple_list, key=last)    

# main
def main():
    tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_tuple_list = get_sorted_list(tuple_list)
    print(sorted_tuple_list)


if __name__ == "__main__":
    main()