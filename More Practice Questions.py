'''
Task 1 - Shopping List Function
Create a function that allows users to add items to a shopping list until they enter "done".
The function should return the complete shopping list when finished.
'''

def create_shopping_list():
    shopping_list = []  # empty shopping list to store items
    adding_items = True   # boolean variable to control the loop
    
    print("Shopping List Creator")
    print("Enter items for your shopping list. Type 'done' when finished.")
    
    while (adding_items):  # condition to continue loop while still adding items
        item = input("Enter the item: ")  # get user input for next item
        
        if (item.lower()=="done"):  # check if user is done adding items
            adding_items = False  # update control variable to exit loop
        else:
            shopping_list.append(item)  # add item to shopping list
    
    return shopping_list  # return the complete shopping list

# Call function to get shopping list
my_shopping_list = create_shopping_list()

# Display shopping list
print("\nYour Shopping List:")
if (len(my_shopping_list)==0):  # check if shopping list is empty
    print("Your shopping list is empty!")
else:
    for item in my_shopping_list:  # loop through items in shopping list
        print(item)  # display each item

# Total for Task 1 (20 marks)





'''
Task 2 - List
Create a program that lets users manage a to-do list, allowing them to add items
and display the current list. The program should continue until the user enters "exit".
'''

# print("To-Do List Manager")
# print("Add items to your to-do list. Type 'exit' when finished, 'show' to display current list.")

# todo_list = "your code here"  # empty to-do list
# continue_program = "your code here"  # boolean to control program execution

# while ("your code here"):  # condition to keep program running
#     command = "your code here"  # get user input
    
#     if ("your code here"):  # check if user wants to exit
#         continue_program = "your code here"  # update control variable to exit
#     elif ("your code here"):  # check if user wants to see current list
#         print("\nCurrent To-Do List:")
#         if ("your code here"):  # check if list is empty
#             print("Your to-do list is empty!")
#         else:
#             # use a loop to display each item with its position number
#             for "your code here" in range("your code here"):
#                 print(f"{i+1}. {todo_list[i]}")
#     else:
#         # add item to list
#         "your code here"
#         print(f"Added: {command}")

# # Display final list
# print("\nFinal To-Do List:")
# if ("your code here"):  # check if list is empty
#     print("Your to-do list is empty!")
# else:
#     for "your code here" in range("your code here"):
#         print(f"{i+1}. {todo_list[i]}")

# Total for Task 2 (20 marks)





'''
Task 3 - Validation Function
Create a function that validates user credentials (username and password).
The function should take username and password as parameters and return True
if credentials are valid, False otherwise. Valid credentials are:
username: "admin" and password: "password123" OR
username: "user" and password: "user2024"
'''

# def validate_credentials(username, password):
#     # Check if credentials match any of the valid combinations
#     if ("your code here"):  # check first valid combination
#         return "your code here"  # return appropriate boolean
#     elif ("your code here"):  # check second valid combination
#         return "your code here"  # return appropriate boolean
#     else:
#         return "your code here"  # return appropriate boolean for invalid credentials

# # Main program
# print("Login System")

# max_attempts = 3
# attempts = 0
# logged_in = "your code here"  # boolean to track login status

# while ("your code here" and "your code here"):  # condition to continue while not logged in and under max attempts
#     # Get user credentials
#     username = "your code here"
#     password = "your code here"
    
#     # Validate credentials using function
#     if ("your code here"):  # call validation function with appropriate parameters
#         print("Login successful!")
#         logged_in = "your code here"  # update login status
#     else:
#         attempts = "your code here"  # increment attempt counter
#         remaining = max_attempts - attempts
#         print(f"Invalid credentials. {remaining} attempts remaining.")

# # Check final login status
# if ("your code here"):  # check if user is logged in
#     print("Welcome to the system!")
# else:
#     print("Maximum login attempts exceeded. Account locked.")

# # Total for Task 3 (20 marks)





'''
Task 4 - Input Validation Loop
Create a program that asks users for their age and validates that it is between 
0 and 120. The program should continue asking until valid input is received.
'''

# print("Age Verification System")
# print("Please enter your age (0-120)")

# valid_data = "your code here"  # boolean to track if valid data has been entered
# age = "your code here"  # initialize age variable

# while ("your code here"):  # loop condition to continue while data is not valid
#     try:
#         # Get user input and convert to integer
#         user_input = "your code here"
#         age = "your code here"  # convert input to integer
        
#         # Check if age is within valid range
#         if ("your code here"):  # check if age is valid (between 0 and 120)
#             print("Valid age entered!")
#             valid_data = "your code here"  # update flag to exit loop
#         else:
#             print("your code here")  # error message for out of range
#     except "your code here":  # catch non-integer inputs
#         print("your code here")  # error message for non-integer input

# # Display final result
# print(f"Thank you! Your age ({age}) has been recorded.")

# # Total for Task 4 (20 marks)





# '''
# Task 5 - Authentication System
# Create a program that authenticates users based on username and password.
# Valid credentials are:
# username: "student1" password: "pass123"
# username: "admin" password: "admin2024"
# The program should give users 3 attempts before locking them out.
# '''

# print("Login System")
# print("You have 3 attempts to log in.")

# # Valid credentials
# valid_users = {
#     "student1": "pass123",
#     "admin": "admin2024"
# }

# attempts_remaining = "your code here"  # initialize number of login attempts
# authenticated = "your code here"  # boolean to track authentication status

# while ("your code here" and "your code here"):  # condition for continuing attempts
#     # Get user credentials
#     username = "your code here"  # get username
#     password = "your code here"  # get password
    
#     # Check if username exists
#     if ("your code here"):  # check if username is in valid_users dictionary
#         # Username exists, check password
#         if ("your code here"):  # check if password matches stored password
#             print("your code here")  # success message
#             authenticated = "your code here"  # update authentication status
#         else:
#             print("your code here")  # password error message
#             attempts_remaining = "your code here"  # decrease attempts
#     else:
#         print("your code here")  # username error message
#         attempts_remaining = "your code here"  # decrease attempts
    
#     # Display remaining attempts if not authenticated
#     if ("your code here" and "your code here"):  # check if not authenticated and attempts remain
#         print(f"Attempts remaining: {attempts_remaining}")

# # Final message based on authentication status
# if ("your code here"):  # check if authenticated
#     print("Welcome to the system!")
# else:
#     print("your code here")  # account locked message

# # Total for Task 5 (20 marks)