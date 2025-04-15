''' 
r=read
w=write(delets everything and over writes)
a=append
x=create new file and poen it for writing
b=binary mode
t= text mode
+ = used for double mode

r+= read and write
w+=write and read
a+=append and read

write rb wb for binary
'''

'''
R
f.read() = reads everything
f.readline() = reads a single line
'''
# f=open('file_name','mode') #default mode is read(r)

# f=open('hi.txt','r')
# data=f.read()
# print(data) #type of data is string
# f.close()

# f=open('hi.txt')
# line1=f.readline()
# line2=f.readline()
# print(line1,line2)

'''Write and Append
Creates a new file if it doesn't exist

'''

# f=open('hi.txt','a')
# f.write("Messi")
# f.close()

'''Read and write (r+)
Over writes the files from start (pointer at start)
Write and Read (w+)
Truncates and writes (pointer at start)
Append and Read (a+)
Writes at last (pointer at end)
'''

'''With syntax
with open('hi.txt','r') as f:
    ...
    ...

no need to close this file and indentation is mandatory
'''





'''os modules
import os
To remove 
os.remove("file_name")

print(os.name)
print(os.getcwd())
print(os.listdir())
# os.mkdir("New")  #To create a new folder(directory)
# os.chdir("Tutorial")  # To change directory
# os.chdir("..") #To go back in directory
# os.rmdir('New')
# os.makedirs("parent/child") #To create nested folder

'''


# Practice
# with open("try.txt","w") as f:
#     f.write("Hi everyone \nthis is a test \nhope your'e ok")
#     f.write("I am learning Java\nJava is a good pl")
# with open("try.txt","r") as f:
#     print(f.read())

#To replace some data
# with open("try.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","Python")
# with open("try.txt","w") as f:
#     f.write(new_data)
# with open("try.txt","r") as f:
#     data=f.read()
#     print(data)


#Check if aword exists in file
# with open("try.txt","r") as f:
#     data=f.read()
#     # if data.__contains__("Python"):
#     # print("YEs")

#     if data.find("Python")!=-1:
#         print("Yes")

#check in which line a word exists
# def check_for_line():
#     word="Python"
#     line=1
#     data=True
#     with open("try.txt") as f:
#         while data:
#             data=f.readline()
#             if word in data:
#                 print(line)
#                 return
#             line+=1
#     return -1
# check_for_line()

def check_for_even():
    count=0
    with open('numbers.txt') as f:
        data=f.read()
        splitted=data.split(",")
        print(splitted)
        for i in splitted:
            if int(i)%2==0:
                count+=1
        print(count)
check_for_even()
