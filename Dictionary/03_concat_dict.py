'''
@Author: shubham shirke
@Date: 2023-06-10 13:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 13:35:30
@Title : Python script to concatenate following dictionaries to create a new one.
'''

def concat_dictionary(dict_elements,dict_elements_2):
    """
    Descripition : 
            This function combines a two or more dictionaries.
    Paremeters  :
            dict_elements : contains dict of elements.
            dict_elements_1 : contains dict of elements.
    Retruns    :
            dict_elements : updated dictionary.
    """
    for key , value in dict_elements_2.items():
        dict_elements[key] = value    

    return dict_elements


# main
def main():
    dict_elements = {0:1,1:2,2:3}
    dict_elements_2 = {3:4,4:5,5:6}
    result_dict_elements = concat_dictionary(dict_elements,dict_elements_2)
    print(f"The dictionary of elements is: {result_dict_elements}")



if __name__ == "__main__":
    main()


