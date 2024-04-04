"""
Created by Angelo John Benedict Laus of SF231
Created on April 4, 2024
"""

print("****************************")
while True:
    try:
        num_inputs = int(input("How many inputs?: "))
        if num_inputs <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a 1+ number only.")
print("****************************")
inputs = []
for _ in range(num_inputs):
    while True:
        try:
            num = int(input("Enter a number: "))
            inputs.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number only.")

print("****************************")
palindromic_numbers = []
for num in inputs:
    num_string = str(num)
    if len(num_string) >= 2 and num_string[0] == num_string[-1]:
        palindromic_numbers.append(num)

print("Look for the input that is \na Palindromic Number: ", end="")
for num in palindromic_numbers:
    print(num, end=" ")
print("\n****************************")


"""
Regarding the use of some methods:
I cannot think of a way that would not require the following methods:
append() == Used to append the input numbers to the list.
len() == Used to check the length of the number to determine the possibility of repeating numbers.

I also applied error checking as its importance was taught during my programming classes with the School of Engineering.
"""
