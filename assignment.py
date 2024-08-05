#this line is edited in github
# def read_and_display_file(filename):
#     try:
#         # Open the file in read mode
#         with open(filename, 'r') as file:
#             # Read the contents of the file
#             content = file.read()
#         # Display the contents of the file
#         print(content)
#     except FileNotFoundError:
#         print(f"The file {filename} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# # Take the filename input from the user
# filename = input("Enter the filename: ")
#
# # Call the function to read and display the file
# read_and_display_file(filename)


# 1) Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
from shlex import join

l=[]
for i in range(2000, 3200):
    if(i%7==0) and (i%5!=0):
        l.append(str(i))
        print(','.join(l))


# 2) Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
#
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

x=int(input())
print(factorial(x))

