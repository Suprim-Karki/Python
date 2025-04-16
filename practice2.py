'''
Mock Lab-Based Practical Instructions

The downloaded file "mock_test.py" must be opend in IDLE editor.

You can use  curated set of notes that accompany this assessment.

There are 5 coding tasks for you to complete.

Eash task details are given at the start of the task and you must write the code where it states

"your code here" to make the task work as intended.


You can run your code from within IDLE to check that it works and edit errors in code.

When all tasks have been completed, save the file and upload it the lab-test folder on Blackboarrd.

Write your name here: Suprim Karki

Write StudentID here: 
''' 


'''
Task 1 - Single attempt: A user must enter a 6-digit code and a secret word that should match stored information

to be able to perform secure transactions. If correct information is entered a message saying "secure transactions allowed" is 

printed, otherwise a message "no transactions allowed". 

Complete code for Task 1:
'''

correct_code = "123789"
secret_word = "mock_test"

# get user information: use input function

user_code =  input("Enter the code")
user_word = input("Enter the word")

# Check if correct information is entered.
# print a suitable message to inform the user.

if(correct_code==user_code and secret_word==user_word): # Write the missing code (condition) in the bracket:   
    print("secure transactions allowed")       
else:                                                             
    print("no transactions allowed")           


'''
Task 2 - Multiple attempts: A user must enter a 6-digit code and a secret word that should match stored information

to be able to perform secure transactions. If correct information is entered a message saying "secure transactions allowed" is 

printed, otherwise a message "no transactions allowed". 

Complete code for Task 2:

'''


valid_data = False # use a boolean variable to track information entered is correct or not:

while (valid_data==False):
    user_code =  input("Enter the code")
    user_word = input("Enter the word")

    if(correct_code==user_code and secret_word==user_word): 
        print("secure transactions allowed")
        valid_data = True
    else:
        print("no transactions allowed")                                        
        

                                                                    # Total for Task 2 (20 marks)

'''
Task 3 - Refactor Task 2 code to use a function.
Modify Task 2 by introducing a function to check user enteterd information.
'''

def check_user_info(code, word):
    if("your code here"):
        return "your code here"
    else:
        return "your code here"
    
# end of function

user_code =  "your code here"
user_word = "your code here"
valid_data = "your code here"
while("your code here"):
    print("no transactions allowd")
    user_code = "your code here"
    user_word = "your code here"
    valid_data = "your code here"
    print()
print("secure transactions allowed") #   
                                                
                                                                     # Total for Task 3 (20 marks)

'''
Task 4 - gift list
Allow users to create a gift until they enter either "n" or "N" and then 
print the list, each gift on a new line.
'''

print("Gift List")
print("this program stores your gift list and then displays it")

gift_list = "your code here"  # empty gift list
add_gift = "your code here" # boolean variable to check if no more gifts are to be added.

while ("your code here"): 
    next_gift = "your code here"
    if ("your code here"):
        # no new gifts
        add_gift = "your code here"
    else:
        # add next_gift  to gift list #
        "your code here"

#display list

print()
print("Gift List Display")
print()
if ("your code here"): # check if gift_list is empty #

    print("No gifts added")
else:
    #use a for loop to iterate through gift_list to display each gift
    "your code here"
                                                    
        
                                                                         #  Total for Task 4 (20 marks)
'''
Task 5 - Refactor Gift List Using a Function
Encapsulate Task 4 into a function add_to_gift_list().
'''

def add_to_gift_list():
    gift_list = "your code here" # create empty gift list
    add_gift = "your code here"


    while ("your code here"):
        next_giftm =  "your code here"
        if ("your code here"):   # write the if condition that checks if user does not want to add any more gifts
            add_gift="your code here"
            return "your code here"
        else:
             "your code here"   #  update gift list

# Call function to get gift list
gift_list = "your code here"

# Display gift list

print("\nGift List:")
if ("your code here"):
    print("your code here")
else:
    "your code here"


                                                                        # Total for Task 5: (20 marks)
