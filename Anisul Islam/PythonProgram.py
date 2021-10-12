# Python Programming is Starting 10.10.2021

# print("Tipu Sultan")
# print("01949212011")

# Comment
# ======================================
# This is a single line comment
'''
This is a 
multiple
line comment
'''

# Backslash character
# ======================================
# print("Tipu Sultan \n 011695545644")   # new line
# print("Tipu Sultan \t 011695545644")
#
# print("\"Tipu\"")

# Variable
# ===========================================
# name = "Tanvir"
# age = 23
# print("Our new student is " + name)
# print(name + " lives in Dhaka")
# print("He is currently", age, "lives in Doha")
# print(name + " is now ", age, " years old")
#
# print("TIPU " + "Sultan " + " Tanvir")

# Basic Numerical Operations
# ==============================================
# print(11+4)
# print(11-4)
# print(11*4)
# print(11/4)
# print(11%4)
#
# a = 27
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
#
# print(a//b)  # floor means 4.5~4
#
# print(4**3)

# Getting User input
# =========================================

# name = input("enter name: ")
# age = input("ENter age: ")
# gpa = input("ENter gpa: ")
#
# print("Student information")
# print("---------------------")
# print("Name : "+name)
# print("age : "+age)
# print("gpa : "+gpa)

# Type casting
# ===================================

# num1 = input("Enter first number: ")
# num2 = input("Enter first number: ")
#
# sum = int(num1) + int(num2)
# print("The sum is ",sum)
# -------------------------------------------------
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter first number: "))
#
# result = num1 + num2
# print("The result is ", result)
#
# result = num1 - num2
# print("The result is ", result)

# Area of any shape
# ======================================

# base = float(input("ENter base: "))
# height = float(input("Enter height: "))
#
# Triangle = 0.5 * base * height
# print("Triangle =",Triangle)

# Math related library function
# =====================================

# from math import *
#
# print(max(20,10))
# print(min(20,10))
# print(abs(-4))
# print(pow(2,3))
# print(sqrt(25))
# print(round(3.4))
# print(round(3.5))
# print(round(3.9))
# print(floor(3.7))
# print(ceil(3.3))

# Formatted String : Type Function
# ================================================
# num = 20
# print(type(num))
# num2 = 20.5
# print(type(num2))
# name = "TIpu"
# print(type(name))
# print(type(True))

# Formatted string
# ===================================

# num1 = 20
# num2 = 30
# print(f"{num1} + {num2} = {num1+num2} ")
#
# print("TIpu Sultan")
# print("201565544555f")
#
# print("TIpu Sultan ", end="")
# print("201565544555f")

# Relational Operator and Boolean data type
# ============================================

# print(30 > 20)
# print(30 >= 20)
# print(30 <= 20)
# print(30 < 20)
# print(30 == 20)
# print("Anis" == "Anis" )

# IF elif else statement
# ==========================

# mark = 50
# if mark>=33:
#     print("Pass")
#
# if mark < 33:
#     print("Fail")
# -----------------------------
# mark = 50
# if mark >= 33:
#     print("Pass")
# else:
#     print("Fail")
# ---------------------------
# mark1 = -20
# mark2 = 50
#
# if mark1 >= mark2:
#     print("Pass")
# else:
#     print("Fail")
# ________________________________
# even odd

# num = 6
#
# if num%2 == 0:
#     print("even")
# else:
#     print("odd")

# --------------------------------------

# marks = 24
# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C")
# elif marks >= 40:
#     print("D")
# elif marks >= 30:
#     print("E")
# else:
#     print("Fail")
#     print("TRy next time")

# Inner if statement
# ======================================

# if 7>6:
#     if 7>7:
#         print("HI")
#     else:
#         print("not work")

# -----------------------------------------------

# num1 = -1
# num2 = 8
# num3 = 7

# if num1 > num2:
#     if num1 > num3:
#         print("Big num1")
#     else:
#         print("num3")
#
# else:      # we can use here  = else:
#     if num2 > num3:
#         print("big num2")
#     else:
#         print("big num3")

# ---------------------------------------------------------

# num1 = 50
# num2 = 30

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)
# ------------------------------------------
# Ternary operator

# print(num1 if num1>num2 else num2)
#
# max = num1 if num1>num2 else num2
# print("maximum = ", max)
# ------------------------------------------------
# logical operator

# num1 = 20
# num2 = 30
# num3 = 50
#
# if num1> num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)
# ------------------------------------------
# vowel consonant check:

# ch = 'o'
# if ch == 'a' or ch == 'e' or ch == 'i' or ch == "o" or ch == 'u':
#     print("vowel")
# else:
#     print("consonant")
# --------------------------------------------------

# letter grade program

# marks = 65
#
# if marks >= 80 and marks <= 100 :
#     print("A+")
# elif marks >= 70 and marks <= 79:
#     print("A")
#
# # we can also write
# if 60 <= marks <= 69:
#     print("A-")

# While loop
# ==============================

# i = 1
# while i <= 20:
#     print(i)
#     i = i + 1
# print("ENd")

# i = 2
# while i <= 20:
#     print(i)
#     i = i + 2
# print("ENd")

i = 1
while i <= 20:
    print(i)
    i = i + 2
print("ENd")