'''
@Author: shubham shirke
@Date: 2023-06-10 13:28:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 13:28:30
@Title : Python script to sort (ascending and descending) a dictionary by value.
'''

def get_dictionary(elements):
    """
    Descripition : 
            This function returns ascending and descending value from the dictionary.
    Paremeters  :
            elements : contains set of elements from the dictionary.
    Retruns     :
            ascend_dict
            descend_dict
    """
    # lambda is simple expression anonymous function 
    ascend_dict = sorted(elements.items(),key=lambda x: x[1])  
    descend_dict = sorted(elements.items(),key=lambda x: x[1],reverse=True)

    return ascend_dict , descend_dict


# main
def main():
    dict_elements = {'one':1,'two':2,'three':3}
    ascend , descend = get_dictionary(dict_elements)
    print(f"The dictionary in ascendng order is: {ascend}")
    print(f"The dictionary in descendng order is: {descend}")



if __name__ == "__main__":
    main()


