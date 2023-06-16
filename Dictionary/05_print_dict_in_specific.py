'''
@Author: shubham shirke
@Date: 2023-06-10 14:39:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-10 14:39:30
@Title : Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''

def get_dictionary_items(number):
    """
    Descripition : 
            This function creates a dictionary that contains a number (between 1 and n) in the form (x, x*x).
    Paremeters  :
            number : value till where dictionary to generate. 
    Retruns    :
            new_dict  : dictionary in the specified form.
    """
    new_dict = {}

    # iterating over the new_list to store values in it.
    for item in range(1,number+1):
            new_dict[item] = item**2

    return new_dict


# main
def main():
    number = int(input("Enter final range number for dictionary: "))
    new_dict = get_dictionary_items(number)
    print(f"The result dictionary is: {new_dict}")



if __name__ == "__main__":
    main()


