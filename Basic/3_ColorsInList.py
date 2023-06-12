'''
@Author: shubham shirke
@Date: 2023-06-06  22:40:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-06 22:40:30
@Title : Python program to display the first and last colors from the following colors list.
'''


def colors_in_list():
    """
    Description : This function prints first and last colors of the colors list using their index numbers.
    Parameters : none
    Result : First and last color of the colors list.
    """
    colors = ["Red","Green","White" ,"Black"]
    print(f"First-color:{colors[0]}")
    print(f"Last-color:{colors[-1]}")


# main
def main():
    colors_in_list()


if __name__ == "__main__":
    main()