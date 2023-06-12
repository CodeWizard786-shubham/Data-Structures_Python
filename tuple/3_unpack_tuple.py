'''
@Author: shubham shirke
@Date: 2023-06-09 21:43:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-09 21:43:30
@Title : python program to create a tuple with different data types.
'''


def unpack_tuple(list_elements):
    """
    Description : 
            This function seperates tuple elements into different variables.
    Parameters : 
            list_elements : list of elements.
    Returns : 
            none
            prints values and type of variable.
    """
    tuple_of_elements = tuple(list_elements)
    var1 , var2 , var3 , var4, var5 ,var6= tuple_of_elements

    print (f"var_1: {var1} and type is : {type(var1)}")
    print (f"var_2: {var2} and type is : {type(var2)}")
    print (f"var_3: {var3} and type is : {type(var3)}")
    print (f"var_4: {var4} and type is : {type(var4)}")
    print (f"var_5: {var5} and type is : {type(var5)}")
    print (f"var_6: {var6} and type is : {type(var6)}")

# main
def main():
    list_elements = [1,2.3,'hello','world',6+3j,True]
    unpack_tuple(list_elements)


if __name__ == "__main__":
    main()
