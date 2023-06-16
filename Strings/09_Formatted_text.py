'''
@Author: shubham shirke
@Date: 2023-06-08 10:05:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-08 10:05:30
@Title : Python program to display formatted text (width=50) as output.
'''
import textwrap

def formatted_text(text):
    """
    Description : 
            This function formats text to 50 characters per line using 'textwrap.fill' function.
    Parameters : 
            text - input text
    Return :
            returns nothing 
            print formatted text.
    """
    print(textwrap.fill(text, width=10))

# main
def main():
    text = '''
  Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such as C++ or Java.
  '''
    formatted_text(text)


if __name__ == "__main__":
    main()
