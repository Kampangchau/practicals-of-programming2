"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the content of the input a invalid number.
Nor can other similar special digital.
2. When will a ZeroDivisionError occur?
The denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")