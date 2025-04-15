#1.

# i=1
# while(i<6):
#     print(i)
#     i+=1

# 2.

# sum=0
# i=1
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

# 3
# i=1
# while i<6:
#     print(i)
#     if(i==3):
#         break
#     i+=1

# 4
# i=0
# while i<6:
#     i+=1
#     if(i==3):
#         continue
#     print(i)

# 6.
# email="test@test.com"
# password = "changeMe"
# attempt=0
# while True:
#     u_email = input("Enter email ")
#     p_input = input("Enter password ")
#     if(email==u_email and password==p_input):
#         print("successful login")
#         print(f"You made {attempt} attempts")
#     else:
#         print("Invalid email or password")
#         attempt+=1
#     if attempt==3:
#         print("Account locked - contact administrator")
#         break

# 9
# email="test@test.com"
# password = "changeMe"
# attempt=0
# while True:
#     u_email = input("Enter email ")
#     if(email==u_email):
#         p_input = input("Enter password ")
#         if ( p_input==password):
#             print("Successful Login")
#             print(f"You made{attempt} attempts")
#             break
#         else:
#             print("Invalid password")
#             attempt+=1
#     else:
#         print("Invalid email")
#         attempt+=1
#     if attempt==3:
#         print("Account locked - contact administrator")
#         break

# 10
# a="hello"
# for i in a:
#     print(i)

# 11   
# a="hello"
# length =0 
# for i in a:
#     length+=1
# print(length)


# 12
# a="hello"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# 16
# x – 2y + 3z = 5
# for x in range(11):
#     for y in range(11):
#         for z in range(11):
#             if (x-2*y+3*z) == 5:
#                 break
# print(f"x = {x}")
# print(f"y = {y}")
# print(f"z = {z}")

# 17
# x – 2y + 3z = 5
# z=(5-x+2y)/3
# for x in range(11):
#     for y in range(11):
#         z=(5-x+2*y)/3
#         if(z.is_integer()==True) and (z>=0 and z<11):
#             print(f"Solution: x={x}, y={y} and z={z}")


# # 1. Write a program that takes a full name as input (e.g., ”John Doe Smith”) and extracts
# # the initials of the first and last names.

# name = input("Enter your name: ")
# split_name = name.split(" ")
# first = split_name[0]
# last = split_name[-1]
# answer = first[0].upper() +"." +last[0].upper() + "."
# print(answer)

# # 2. Write a program that formats a phone number. The user inputs a 10-digit phone
# # number as a single string (e.g., ”1234567890”). Your program should format it as ”(123) 456-7890

# ph_number = input("Enter your number: ")
# if (len(ph_number) != 10):
#     print("The phone number is invalid")
# print(f"({ph_number[:3]}) {ph_number[3:6]}-{ph_number[6:]}")

# # 3. Write a program that takes a string input from the user and returns the string re-
# # versed using string slicing

# string = input("Enter a string: ")
# reversed = string[::-1]
# print(reversed)

# # 4. Write a program that takes an email address as input (e.g., ”user@example.com”)
# # and extracts the domain (the part after the @).

# email_address = input("Enter your email: ")
# split = email_address.split("@")
# domain = split[-1]
# print(domain)

# # 5. Write a program that checks if a given string is a palindrome (reads the same forward
# # and backward). Ignore spaces, punctuation, and case.

# string =  input("Enter a string: ")
# add = ""
# for i in string:
#     if i.isalnum():
#         add += i.lower()
# if add == add[::-1]:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")


# # 6.  Write a program that checks if a specific substring exists within a given string. The
# # user will input both the main string and the substring. If the substring is found, print its starting
# # index.

# str = input("Enter an string: ")
# sub_str = input("Enter a sub-str: ")
# if string.find(sub_str) != -1:
#     index = string.find(sub_str)
#     print("The substring provided exists")
#     print(f"It stats at {index} index")
# else:
#     print("Substring does not exist")

# # 7.Write a program that analyzes a line from a CSV (Comma-Separated Values) file.
# # The program should take a string representing a CSV line (e.g., ”John,Doe,30,Male”) and extract
# # each field.

# CSV = input("Enter CSV: ")
# items=CSV.split(",")
# print(f"First Name: {items[0]} \nLast Name: {items[1]} \nAge: {items[2]} \nGender: {items[3]}")

list=[]
while True:
    item = input("Enter an item: ")
    if item=="":
        break
    list.append(item)
print(list)
