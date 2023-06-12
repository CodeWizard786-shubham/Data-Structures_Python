'''
@Author: shubham shirke
@Date: 2023-06-07  14:15:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 14:15:30
@Title :  Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
'''

def print_colors_from_set():
    """
    Description : 
            This function print out a set containing all the colors from color_list_1 which
            are not present in color_list_2.
    Paraments : 
            none
    Result :
            color_list_3 : which is difference between color_list_1 and color_list_2 
    """
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    color_list_3 =set()

    color_list_3 = set(color_list_1) - set(color_list_2)

    print(color_list_3)


def main():
    print_colors_from_set()


if __name__ == "__main__":
    main()