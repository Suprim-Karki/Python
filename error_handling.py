'''
Error handling = An event that interrupts the flow of a program
                1. ZeroDivisionError,
                2. TypeError (Eg: int("Pizza)) 
                3. ValueError(Eg: 1+"1") 

                Methods
                1. try 
                2. except {exception}
                3. finally

'''
try:
    num = int(input("Enter a number"))
    print(1/num)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("You can't divide by 0 moron")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup")