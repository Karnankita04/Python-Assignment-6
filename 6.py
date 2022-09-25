# 1. Write a python script to check whether a given number is positive or non-positive
# code: 
# n=int(input("Enter a number"))
# if n>0:
#     print("Positive")
# else:
#     print("non-positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not
# code: 
# n=int(input("Enter a number "))
# if n%5==0:
#     print("Divisible")
# else:
#     print("Not divisible")
# one line 
# print("Divisible by 5" if int(input("Enter a number"))%5==0 else "Not Divisible by 5")

# 3. Write a python script to check whether a given number is even or odd
# code: 
# n=int(input("Enter a number "))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")
# print("Odd" if (int(input("Enter a number: ")))%2 else "True")

# 4. Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.
# num1=int(input("Enter a number"))
# num2=int(input("Enter another number"))
# if num1>=num2:
#     print(num1,"is greater")
# else:
#     print(num2,"is greater")

# single line if else
# print("Enter two numbers: ")
# a,b=int(input()),int(input())
# print(a if a>b else b)

# 5. Write a python script to print two given words in dictionary order
# code: 
# print("Enter two words: ")
# a,b=input(),input()
# print(a if a<b else b)

# 6. Write a python script to check whether a given number is a three digit number or not.
# code: 
# n=int(input("Enter a number: "))
# print("three digit number" if 99<n<1000 else "Not a three digit number")

# 7. Write a python script to check whether a given number is positive, negative or zero.
# code: 
# n=int(input("Enter a number"))
# if n>0:
#     print(n,"is positive number")
# elif n==0:
#     print(n,"is zero")
# else:
#     print(n,"is negative number")
# print()

# 8. Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots 
# code: 
# print("Enter value of a,b,c of a quadratic equation")
# a,b,c = int(input()),int(input()),int(input())
# d=b**2-4*a*c
# if d>0:     
#     print("Real and distinct roots")
# elif d==0:
#     print("Real and equal roots")
# else:
#     print("Imaginary roots")

# 9. Write a python script to check whether a given year is a leap year or not.
# code: 
# n=int(input("Enter the year: "))
# if n%400 == 0:
#     print("Leap year")
# elif n%100!=0 and n%4==0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
# code: 
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number"))
# print((num1 if num1>num3 else num3)    if num1>num2  else(num2 if num2>num3 else num3))

# if num1>num2:
#     if num1>num3:
#         print(num1,"is the greatest number")
#     else:
#         print(num3,"is the greatest number")
# elif num2>num3:
#     print(num2,"is the greatest number")
# else:
#     print(num3,"is the greatest number")

# 11. Write a python script to take the month value in numeric format and display the number of days in it.
# code: 
# month=int(input("Enter the month value in numeric format: "))
# if month in (1,3,5,7,8,10,12):
#     print("31 days")
# elif month in (4,6,9,11):
#     print("30 days")
# elif month==2:
#     print("28 or 29 days")
# else:
#     print("invalid number")

# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
# code: 
# x=complex(input("Enter a complex number: "))
# print(x.real if x.real>x.imag else x.imag)

