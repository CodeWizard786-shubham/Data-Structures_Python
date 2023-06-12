'''
@Author: shubham shirke
@Date: 2023-06-07  09:35:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-07 09:35:30
@Title : Python program to print documentation in built_in python functions.
'''

def print_function_doc(func_name):
    """
    Description : This function prints the documentation of python built-in functions.
    Parameters : 
        func_name - name of the python built_in function
    Result    : documentation
    """
    print(f"Documentation for {func_name}")
    print()
    print(func_name.__doc__)
    #help(func_name)

# main
def main():
    func_name =eval(input("Enter function name: "))
    print_function_doc(func_name)

if __name__ == "__main__":
    main()