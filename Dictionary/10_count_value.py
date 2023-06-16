'''
@Author: shubham shirke
@Date: 2023-06-10 18:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 18:30:30
@Title : Python program to count the values associated with key in a dictionary.
'''

def get_count_of_values(dict_elements):
    """
    Descripition : 
            This function iterates over input list to find it any item in list is success having value as True. 
    Paremeters  :
            dict_elements : input dictionary from user. 
    Retruns    :
            count : returns count where success is true.
    """
    count = 0
    for items in dict_elements:
        if items.get('success') == True:
            count += 1

    return count

    # main
def main():
    dict_elements =  [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    result_count = get_count_of_values(dict_elements)
    print(f"Count of items with success as True: {result_count}")



if __name__ == "__main__":
    main()









