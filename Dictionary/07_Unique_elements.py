'''
@Author: shubham shirke
@Date: 2023-06-10 17:20:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 17:20:30
@Title : Python program to print all unique values in a dictionary
'''

def get_dictionary_items(dict_elements):
    """
    Descripition : 
            This function iterates over the dictonary to get values and store them into a set containing unique values.
    Paremeters  :
            dict_elements : This contains a list of different dictionary key , value items. 
    Retruns    :
            unique_values : returns a set containing unique values.
    """
    unique_values = set()

    for item in dict_elements:
        for value in item.values():
            unique_values.add(value)
    return unique_values

# main
def main():
    dict_elements = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    unique_values = get_dictionary_items(dict_elements)
    print(f"The result dictionary is: {unique_values}")



if __name__ == "__main__":
    main()









