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

# i = 1
# while i <= 20:
#     print(i)
#     i = i + 2
# print("ENd")

# sum of n numbers
# ------------------------------------------

# n = int(input("ENter number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print(sum)

# 2 + 4 + .........+ n

# n = int(input("Enter num: "))
# sum = 0
# i = 2
# while i <= n:
#     sum = sum + i
#     i += 2
# print(sum)

# 3 + 5 + ...............+ n

#
# n = int(input("Enter num: "))
# sum = 0
# i = 3
# while i <= n:
#     sum = sum + i
#     i = i + 2
# print(sum)

# break and continue
# =======================================

# i = 1
# while i <= 100:
#     if i == 20:
#         break
#     print(i)
#     i += 1
# print("End")

# i = 1
# while i <= 100:
#     print(i)
#     i += 1
#     if i == 20:
#         break
# print("End")

# continue

# i = 1
# while i <= 100:
#     if i == 20:
#         continue
#     print(i)
#     i += 1
# print("End")

# OR

# i = 1
# while i <= 30:
#     print(i)
#     i += 1
#     if i == 20:
#         continue
#         print("Continue")
#     print("if")
# print("End")

# LIST
# ========================================

# subjects = ["c", "c++", "Java", "Python", "Android"]

# print(subjects)
# print(subjects[2])
# print(subjects[2:])       # starts from 2 and print all
# print(subjects[-2])

# print("Python" in subjects)
# print("Swift" in subjects)
#
# print("Swift" not in subjects)
#
# print(subjects + ["Swift", 27])
# print(subjects * 3)

# subjects = ["c", "c++", "Java", "Python", "Android"]
# print(len(subjects))
#
# subjects.append("TOC")
# print(subjects)
#
# subjects.insert(2, "OS")
# print(subjects)
#
# subjects.remove("Java")
# print(subjects)
#
# subjects.sort()
# print(subjects)
#
# subjects2 = [10, 90, 30, 40, 80, 60]
# subjects2.sort()
# print(subjects2)
#
# subjects2.reverse()
# print(subjects2)
#
# subjects2.pop()
# print(subjects2)
#
# subjects2.clear()
# print(subjects2)
#
# subjects3 = subjects.copy()
# print(subjects3)

# subjects2 = [10, 90, 40, 40, 80, 40]
#
# pos = subjects2.index(80)
# print(pos)
#
# pos = subjects2.count(40)
# print(pos)

# range function
# ==========================

# num = list(range(10))
# print(num)
# print(num[2])
#
# num = list(range(5, 11))
# print(num)
#
# num = list(range(2, 101, 2))
# print(num)

# for loop
# ===========================================

# num = [10, 20, 30, 40, 50]
# print(num)
#
# index = 0
# n = len(num)
# while index<n:
#     print(num[index])
#     index += 1
# -------------------------------------------------
# num = [10, 20, 30, 40, 50]
#
# for x in num:
#     print(x)
#
# sum = 0
# for x in num:
#     sum += x
# print(sum)

# Series:
# ========================================

# 1 + 2 + 3 + .....................+ n

# n = int(input("Enter the las number: "))
# sum = 0
#
# for x in range(1,n+1,1):
#     sum += x
# print(sum)

# 2+ 4+ 6+ .............+ n

# n = int(input("Enter n: " ))
# sum = 0
# for x in range(2, n+1, 2):
#     sum += x
# print(sum)
# ----------------------------------------
# # 1**2 + 2**2 + 3**2 + .........+ n**2
# n = int(input("Enter n: "))
# sum = 0
# for x in range(1, n+1, 1):
#     sum += x*x
# print(sum)

# ------------------------------------------------

# 1*2*3*..................n

# n = int(input("Enter n"))
# sum = 1
# for x in range(1, n+1, 1):
#     sum = sum*x
# print(sum)

# Pattern
# ===========================================

# n = 3
# for i in range(n+1):
#     print(i*"*")

# ----------------------------------------------
# n =3
# for i in range(n+1):
#     print((2*i-1)*"*")
# ------------------------------------------------
#
# n = 5
# for i in range(n+1):
#     print(i*"*")

# Guessing game
# ==============================================================
# import random
# from random import randint
# guessNumber = int(input("Enter your guess number: "))
# randomNumber = randint(1,5)
#
# if guessNumber == randomNumber:
#     print("Won")
# else:
#     print("Loss")
#     print("Random number: ", randomNumber)
from random import randint

# for x in range(1,6):
#     guessNumber = int(input("Enter your guess number: "))
#     randomNumber = randint(1, 5)
#
#     if guessNumber == randomNumber:
#         print("Won")
#     else:
#         print("Loss")
#         print("Random number :", randomNumber)

 # ======================================================

# list as input from user

# n = input("Enter number: ")
# list = n.split()
# sum = 0
#
# for num in list:
#     sum += int(num)
# print(sum)

# ---------------------------------------------------
#
# numberOfWords = 0
# numOfLetters = 0
# numOfDigits = 0
#
# text = input("Enter a text: ")
# for x in text:
#     x = x.lower()
#     if x >= "a" and x <= "z":
#         numOfLetters += 1
#     elif x >= "0" and x <= "9":
#         numOfDigits += 1
#     elif x == ' ':
#         numberOfWords += 1
# print("Number of letters: ", numOfLetters)
# print("Number of digits: ", numOfDigits)
# print("Number of words ", numberOfWords + 1)

# Matrix
# ======================================================

# matrix = [
#     [1,2,3],
#     [4,5,6],
# ]
# # matrix[0][1] = 10
# # print(matrix[0][1])
#
# for row in matrix:
#     for col in row:
#         print(col)

# Dictionaries:
# ==================================================

# studentId = {
#     "101": "Tipu Sultan",
#     "102": "Maruf Hasan",
#     "103": "Tanvir Sultan",
# }
# # print(studentId["103"])
# # print(studentId.get("102"))
# # print(studenDtId.get("106", "Not a valid key"))
# print(studentId.get("103", "Not a valid key"))
#

# studentId = {
#     101: "Tipu Sultan",
#     102: "Maruf Hasan",
#     103: "Tanvir Sultan",
# }
# # print(studentId["103"])
# # print(studentId.get("102"))
# # print(studenDtId.get("106", "Not a valid key"))
# print(studentId.get(103, "Not a valid key"))

# Tuples
# =======================================

# students = (
#     ("Tipu Sultan", 27, 4.4),
#     "Rabeya Begum",
#     "Nusrat Sultan"
# )
# # students[0] = "MOinul"
# # can not change the value of tuples
# # print(students[0])
# # print(students)
# print(students[1:])

# SET:
# ==================================================

# num1 = {1,2,3,4,5}
# num2 = set([4,5,6])
# print(num2)
# num2.add(7)
# print(num2)
# num2.remove(7)
# print(num2)
#
# print(7 in num2)
# print(4 in num2)
# print(4 not in num2)

# num1 = {1,2,3,4,5}
# num2 = set([3,4,5,6])
#
# print(num1 | num2) # union
# print(num1 & num2)  # intersection
# print(num1 - num2)  # difference

# Stack
# ==================================================

# books = []
# books.append("Learn C")
# books.append("Learn C++")
# books.append("Learn Java")
# print(books)
#
# books.pop()
# print(books)
# print("Now the top book is : ",books[-1])
# # Here LIFO is used
# books.pop()
# print(books)
# print("Now the top book is : ",books[-1])
#
# books.pop()
# if not books:
#     print("No books left")

# Queue
# ========================================================
# bank = ["x", "y", "z"]
#
# from collections import deque
#
# bank = deque(["Anis", "Karim", "Bijoy"])
# print(bank)
# bank.popleft()
# print(bank)
# bank.pop()
# print(bank)
# bank.pop()
#
# if not bank:
#     print("No person left")


# Function
# ===========================================

# a = 20
# b = 10
# sum = a + b
# print(sum)

# def add(a, b, c):
#     sum = a + b + c
#     print(sum)
#
# add(20, 30, 40)

# def message():
#     print("No parameter")
#
# message()

# Returning value from function
# ====================================================

# def add(a, b):
#     sum = a + b
#     return sum
# result = add(20, 30)
# print("result", result)

# def large(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(large(100,300))
#
# maximum = large
# print(maximum(2,3))

# xargs
# ============================================

# def student(id,name):
#     print(id, name)
# student(101,"tipu")

# def student(*details):
#     print(details)
#
# student(101, "Anis")
# student(101, "TIpu", 3.33)
# ---------------------------------------------
# def student(*details):
#     print(details[0])
#
# student(101, "Anis")
# student(101, "TIpu", 3.33)

# def add(num1,num2):
#     sum = num1 + num2
#     print(sum)
#
# add(10,20)
# add(10,20,30)  # not work

# def add(*numbers):
#     print(numbers)
#
# add(10,20)
# add(10,20,30)
# add(10,20,30,90)

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num
#     print(sum)
#
# add(10,20)
# add(10,20,30)
# add(10,20,30,40)

# xxxargs
# ============================================

# def student(**details):
#     print(details)
#
# student(id=101, name="tipu", gpa = 3.45)

# def student(**details):
#     print(details["id"])
#
# student(id=101, name="tipu", gpa = 3.45)
# student(id=102, name="dipu", gpa = 3.5)

# Debugging
# ==================================================

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum += num
#     return sum
# print(add(10,20))

# wrond function

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum += num
#         return sum
# print(add(10,20))

# lambda Functions
# ==================================================

# def calculate(a,b):
#     return a*a + 2*a*b + b*b
# print(calculate(2,3))

# print((lambda a,b : a*a + 2*a*b + b*b)(2,3))
#
# def cube(x):
#     return x*x*x
# print(cube(3))
#
# print((lambda a: a*a*a)(3))

# MAP
# ===============================================

# def square(x):
#     return x*x
#
# num = [1,2,3,4,5]
#
# result = list(map(square,num))
# print(result)

# Filter
# ================================================
#
# num = [1,2,3,4,5]
#
# result = list(filter(lambda x: x%2==0,num))
# print(result)

# List comprehensive
# ==================================================

# num = [1,2,3,4,5]
# result = list(map(lambda x: x*x,num))
# print(result)
# [expression for item in list]

# simple way
# num = [1,2,3,4,5]
# result = [x*x for x in num]
# print(result)

# num = [1,2,3,4,5]
#
# result = list(filter(lambda x: x%2==0,num))
# print(result)

# # simple way
# num = [1,2,3,4,5]
# result = [x for x in num if x%2==0]
# print(result)

# Zip function
# =====================================================

# roll = [101,102,103,104]
# name = ["Tipu", "Anisul", "Dipu", "Numan"]
#
# result = list(zip(roll,name,"ABCDEFGH"))
# print(result)

# Recursion:
# ===============================================

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

# Reading a file
# ==================================================

# file = open("student.txt","r+")
#print(file.writable())
# text = file.read()
# print(text)
# size = len(text)
# print(size)

# text = file.readlines()[0]
# print(text)
#
# file.close()

# for line in file:
#     print(line)
#
# file.close()

# writing a file
# ===================================================

# file = open("student.txt","a")
#
# file.write("\nMaruf - Network engineer")
#
# file.close()
# ----------------------------------------------------
# file = open("student1.txt","w")
#
# file.write("\nMaruf - Network engineer")
#
# file.close()

# file = open("student1.html","w")
#
# file.write("<h1>This is a text</h1>")
#
# file.close()

# Exception Handling
# =================================================

# num2 = int(input("Enter a number: "))
# result = 20/num2
# print(result)
# print("Done")
# ---------------------------------------------

# text = "Tipu"
# print(text[4])
# print("Done")
# ------------------------------------------------

# try:
#     list = [20, 0, 30]
#     result = list[0] / list[3]
#     print(result)
#     print("Done")
# except TypeError:
#     print("Dividing by zero is not possible")
# except IndexError:
#     print("Index Error")
# finally:                            # must work
#     print("Successful")

# -----------------------------------------

# try:
#     num1 = int(input("Enter f number: "))
#     num2 = int(input("Enter s number: "))
#     result = num1/num2
#     print(result)
#
# except ValueError:
#     print("You have to insert only integer")
# except ZeroDivisionError:
#     print("You can not divide a number by 0")
#
# finally:
#     print("Thanks ")

# Do the above error shortly

# try:
#     num1 = int(input("Enter f number: "))
#     num2 = int(input("Enter s number: "))
#     result = num1/num2
#     print(result)
#
# except (ValueError, ZeroDivisionError):
#     print("You have entered incorrect input")
#
# finally:
#     print("Thanks ")

# raise keyword
# =============================================

# def voter (age):
#     if age < 18:
#         raise ValueError("Invalid Voter")
#     return "You are allowed to vote"
#
# try:
#     # print(voter(19))
#     print(voter(17))
# except ValueError as error:     # or can write e
#     print(error)

# swapping
# ====================================================

# a = 20
# b = 10
# temp = a  # temp = 20
# a = b    # a = 10
# b = temp    # b = 20
#
# print("a = ", a)
# print("b = ", b)

# Easy way
# --------------------------------------------

# a = 10
# b = 20
# print("a = ", a)
# print("b = ", b)


# Python OOP
# ====================================================
# ====================================================

# class Student:
#     roll = ""
#     gpa = ""
#
# rahim = Student()
#
# # print(isinstance(rahim,Student))
#
# rahim.roll = 101
# rahim.gpa = 3.23
# print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")
#
# karim = Student()
# karim.roll = 102
# karim.gpa = 4.00
# print(f" Roll : {karim.roll}, GPA : {karim.gpa}")

# Introducing Method
# =====================================================

# class Student:
#     roll = ""
#     gpa = ""
#
#     def set_value(self,roll,gpa):
#         self.roll = roll
#         self.gpa = gpa
#
#     def display(self):
#         print(f"Roll : {self.roll}, GPA : {self.gpa}")
#
#
# rahim = Student()
# rahim.roll = 101
# rahim.gpa = 3.23
# rahim.display()
#
# karim = Student()
# karim.roll = 102
# karim.gpa = 4.00
# karim.display()

# ---------------------------------------------------
# more easily using method

# class Student:
#     roll = ""
#     gpa = ""
#
#     def set_value(self, roll, gpa):
#         self.roll = roll
#         self.gpa = gpa
#
#     def display(self):
#         print(f"Roll : {self.roll}, GPA : {self.gpa}")
#
#
# rahim = Student()
# rahim.set_value(101, 3.45)
# rahim.display()
#
# karim = Student()
# karim.set_value(102, 3.23)
# karim.display()

# Constructor
# ===================================================

class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student(101, 3.45)
rahim.display()

karim = Student(102, 3.23)
karim.display()
