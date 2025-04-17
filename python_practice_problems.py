'''
Conditions, Loops, and Basic String Manipulation
'''

'''1. Check if a Number is Prime
Write a program that takes a number from the user and checks if it is a prime number. If the
number is prime, print ”The number is prime”; otherwise, print ”The number is not prime.”'''

# n=int(input("Enter a number\n"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print("Prime")
# else:
#     print("Not prime")



'''2. Factorial Calculation Using a Loop
Ask the user to enter a positive integer and write a program to calculate its factorial using a
for loop. Display the result.'''

# n=int(input("Enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

'''3. Reverse a String
Write a program that asks the user for a string and then prints the reversed version of that
string. For example, if the input is ”Python,” the output should be ”nohtyP”.'''

# s=input("Enter a string")
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)

'''4. Count Vowels in a String
Ask the user to enter a string and write a program to count the number of vowels (a, e, i, o,
u) in the string. Display the vowel count.'''

# s=input("Enter a string")
# vowels=['a','e','i','o','u']
# c=0

# for i in s:
#     if i.lower() in vowels:
#         c+=1
# print(c)

'''5. Multiplication Table
Write a program that takes a number from the user and prints its multiplication table up to
10. For example, if the user enters 5, the output should display the table of 5 from 5 x 1 to
5 x 10.'''

# num = int(input("Enter a number to see its first 10 multiples: "))

# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

'''6. Sum of Digits of a Number
Write a program that asks the user for a positive integer and calculates the sum of its digits.
For example, if the input is 123, the output should be 6 (1 + 2 + 3).'''

# num = int(input("Enter a number: "))
# sum=0
# temp=0

# while num>0:
#     temp=num%10
#     sum+=temp
#     num=num//10
# print(sum)

'''7. Palindrome Checker
Ask the user for a word and write a program to check if it is a palindrome (reads the same
forward and backward). If it is a palindrome, print ”The word is a palindrome”; otherwise,
print ”The word is not a palindrome.”'''

# s = input("Enter a string: ").lower()
# if s==s[::-1]:
#     print("Palindrome")
# else:
#     print("Not")

'''8. Generate Fibonacci Sequence
Write a program that asks the user for a positive integer n and generates the first n numbers
in the Fibonacci sequence.'''

# a=0
# b=1
# ans=[]
# try:
#     n = int(input("Enter a number: "))
#     if n>0:
#         for i in range(n):
#             ans.append(a)
#             a, b = b, a + b
#     print(ans)
# except ValueError:
#     print("Enter an integer greater than 0")

'''9. Find Minimum and Maximum in a List
Ask the user to enter a list of numbers. Write a program to find and print the smallest and
largest numbers in the list.'''


# nums=input("Enter a list of numbers separated by blank space ")
# try:
#     nums_list=list(map(int,nums.split()))
#     if len(nums_list)==0:
#         print("The list is empty")
#     else:
#         min=nums_list[0]
#         max=nums_list[0]
#         for i in nums_list:
#             if i<min:
#                 min=i
#             elif i>max:
#                 max=i
#     print(f"min = {min} \nmax = {max}")
# except ValueError:
#     print("Enter correct values")

'''10. Word Frequency Counter
Write a program that takes a sentence from the user and counts the frequency of each word.
Display the results as a dictionary where each word is a key and its frequency is the value.
'''

# sentence=input("Enter a sentence: ")
# ans={}
# word_list=sentence.lower().split(" ")
# for word in word_list:
#     if word in ans:
#         ans[word]+=1
#     else:
#         ans[word]=1
# print(ans)

'''Lists, Advanced Loops, and String Operations'''

'''11. Square of Numbers in a List
Write a program that takes a list of integers from the user and returns a new list containing
the square of each number in the original list.'''

# nums=input("Enter a list of numbers separated by space ")
# nums_list=list(map(int,nums.split()))
# ans=[i**2 for i in nums_list]
# print(ans)

'''12. Remove Duplicates from a List
Ask the user to enter a list of numbers, some of which may be duplicates. Write a program
to remove the duplicates and display the list with only unique numbers.'''

# nums=input("Enter a list of numbers separated by space ")
# nums_list=list(map(int,nums.split()))
# ans=[]
# for i in nums_list:
#     if i not in ans:
#         ans.append(i)
# print(ans)



'''13. Merge and Sort Two Lists
Take two lists of integers from the user. Write a program that merges both lists into a single
list and then sorts the merged list in ascending order.'''

# nums1=input("Enter a list of numbers separated by space ")
# nums_list1=list(map(int,nums1.split()))
# nums2=input("Enter a list of numbers separated by space ")
# nums_list2=list(map(int,nums2.split()))

# combined = (nums_list1+nums_list2)
# combined.sort()
# print(combined)

'''14. Count Words of Specific Length
Ask the user to enter a sentence and an integer n. Write a program to count the number of
words in the sentence that have exactly n characters.'''

# sentence=input("Enter a sentence: ")
# n=int(input("Enter the length of word to count: "))
# word_list=sentence.split(" ")
# c=0
# for word in word_list:
#     if len(word)==n:
#         c+=1
# print(c)

'''15. Split a Sentence into Words
Write a program that asks the user for a sentence and splits it into a list of words. Print the
list of words as the output.'''

# sentence=input("Enter a sentence: ")
# word_list=sentence.split(" ")
# print(word_list)

'''16. Capitalize Each Word in a Sentence
Ask the user to enter a sentence and write a program that capitalizes the first letter of each
word in the sentence. Display the modified sentence.'''

sentence=input("Enter a sentence: ")
modified_sentence=""
word_list=sentence.split(" ")
for i,word in enumerate(word_list):
    word = word[0].upper()+word[1:]
    word_list[i]=word
modified_sentence=" ".join(word_list)
print(modified_sentence)

# or just use modified=sentence.title()


'''17. Find the Second Largest Number
Ask the user for a list of integers and write a program to find the second largest number in
the list.'''

'''18. Check for Substring in String
Ask the user to enter a string and a substring. Write a program to check if the substring
exists within the string. If it does, print the starting index of the substring; otherwise, print
”Substring not found.”'''

'''19. Replace a Word in a Sentence
Write a program that asks the user for a sentence, a target word, and a replacement word.
Replace all occurrences of the target word in the sentence with the replacement word and
display the modified sentence.'''

'''20. Concatenate Two Lists Alternately
Ask the user to enter two lists of equal length. Write a program to create a new list by picking
elements alternately from each list. For example, if the input lists are [1, 2, 3] and [’a’,
’b’, ’c’], the output should be [1, ’a’, 2, ’b’, 3, ’c’].
'''