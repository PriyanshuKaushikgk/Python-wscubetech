# ----------------If else statement questions----------------->>>>>>>>>>
# 1. Write a program that takes a user input of three angles and will find out whether it
# can form a triangle or not.

# ans--:
# a1 = int(input("Enter the first angle:-"))
# a2 = int(input("Enter the Second angle:-"))
# a3 = int(input("Enter the Third angle:-"))

# if (a1+a2+a3==180):
#         print("This is a triangle :)")
# else:
#         print("Not triangle :(")


# 2. Arrange string characters such that lowercase letters should come first
# input_str = input("Enter a string: ")

# lowercase_chars = ""
# other_chars = ""

# for char in input_str:
#     if 'a' <= char <= 'z': 
#         lowercase_chars += char
#     else:
#         other_chars += char

# result = lowercase_chars + other_chars

# print("Rearranged string:", result)


# 3. Count all letters, digits, and special symbols from a given string
# a. given-->str1 = "P@#yn26at^&i5ve"
# b. expected-->Total counts of chars, digits, and symbols

# Given string
# str1 = "P@#yn26at^&i5ve"

# # Step 1: Initialize counters
# letter_count = 0
# digit_count = 0
# special_symbol_count = 0

# # Step 2: Extract each character (since there are 16 characters in this string)
# char1 = str1[0]
# char2 = str1[1]
# char3 = str1[2]
# char4 = str1[3]
# char5 = str1[4]
# char6 = str1[5]
# char7 = str1[6]
# char8 = str1[7]
# char9 = str1[8]
# char10 = str1[9]
# char11 = str1[10]
# char12 = str1[11]
# char13 = str1[12]
# char14 = str1[13]
# char15 = str1[14]
# # char16 = str1[15]

# # Step 3: Check each character and increment the respective counters

# # Checking char1
# if 'a' <= char1 <= 'z' or 'A' <= char1 <= 'Z':  # It's a letter
#     letter_count += 1
# elif '0' <= char1 <= '9':  # It's a digit
#     digit_count += 1
# else:  # It's a special symbol
#     special_symbol_count += 1

# # Checking char2
# if 'a' <= char2 <= 'z' or 'A' <= char2 <= 'Z':
#     letter_count += 1
# elif '0' <= char2 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# # Checking char3
# if 'a' <= char3 <= 'z' or 'A' <= char3 <= 'Z':
#     letter_count += 1
# elif '0' <= char3 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# # Similarly check for other characters

# if 'a' <= char4 <= 'z' or 'A' <= char4 <= 'Z':
#     letter_count += 1
# elif '0' <= char4 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char5 <= 'z' or 'A' <= char5 <= 'Z':
#     letter_count += 1
# elif '0' <= char5 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char6 <= 'z' or 'A' <= char6 <= 'Z':
#     letter_count += 1
# elif '0' <= char6 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char7 <= 'z' or 'A' <= char7 <= 'Z':
#     letter_count += 1
# elif '0' <= char7 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char8 <= 'z' or 'A' <= char8 <= 'Z':
#     letter_count += 1
# elif '0' <= char8 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char9 <= 'z' or 'A' <= char9 <= 'Z':
#     letter_count += 1
# elif '0' <= char9 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char10 <= 'z' or 'A' <= char10 <= 'Z':
#     letter_count += 1
# elif '0' <= char10 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char11 <= 'z' or 'A' <= char11 <= 'Z':
#     letter_count += 1
# elif '0' <= char11 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char12 <= 'z' or 'A' <= char12 <= 'Z':
#     letter_count += 1
# elif '0' <= char12 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char13 <= 'z' or 'A' <= char13 <= 'Z':
#     letter_count += 1
# elif '0' <= char13 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char14 <= 'z' or 'A' <= char14 <= 'Z':
#     letter_count += 1
# elif '0' <= char14 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# if 'a' <= char15 <= 'z' or 'A' <= char15 <= 'Z':
#     letter_count += 1
# elif '0' <= char15 <= '9':
#     digit_count += 1
# else:
#     special_symbol_count += 1

# # if 'a' <= char16 <= 'z' or 'A' <= char16 <= 'Z':
# #     letter_count += 1
# # elif '0' <= char16 <= '9':
# #     digit_count += 1
# # else:
# #     special_symbol_count += 1

# # Step 4: Output the total counts
# print("Total letters:", letter_count)
# print("Total digits:", digit_count)
# print("Total special symbols:", special_symbol_count)


#----------ANOTHER METHOD----------------------------

# Given string
# str1 = "P@#yn26at^&i5ve"

# # Initialize counters for letters, digits, and special symbols
# letter_count = 0
# digit_count = 0
# special_symbol_count = 0

# # Loop through each character in the string
# for char in str1:
#     if char.isalpha():  # Check if the character is a letter
#         letter_count += 1
#     elif char.isdigit():  # Check if the character is a digit
#         digit_count += 1
#     else:  # If it's not a letter or a digit, it is a special symbol
#         special_symbol_count += 1

# # Output the total counts
# print("Total letters:", letter_count)
# print("Total digits:", digit_count)
# print("Total special symbols:", special_symbol_count)


str1 = "P@#yn26at^&i5ve"

letter = 0
digit = 0
symbol = 0

for char in str1:
    if char.isalpha():
        letter=letter+1
    elif char.isdigit():
        digit+=1
    else:
        symbol+=1
print(letter)
print(digit)
print(symbol)

