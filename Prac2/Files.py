name_of_user = str(input("Enter your name:"))  # Write code that asks the user for their name,
username_file = 'name.txt'
name_file = open(username_file, 'w')  # then opens a file called "name.txt"
print(name_of_user,file=name_file)  # and writes that name to it.
name_file.close()

name_file = open(username_file, 'r')  # Write code that opens "name.txt" and reads the name (as above) then prints,
print("Yuor name is",name_file.read())  # "Your name is

NUMBERS_FILE = 'numbers.txt'
numbers_file = open(NUMBERS_FILE, 'r')  # opens "numbers.txt",
first_number=int(numbers_file.readline())
second_number=int(numbers_file.readline(2))  #reads only the first two numbers
result = first_number + second_number  # adds them together then prints the result, which should be... 59
print(result)

number_list = []
NUMBERS_FILE = 'numbers.txt'
numbers_file = open(numbers_file, 'r')
numbers = numbers_file.readlines()
for number in numbers:
    number = number.strip("\n")
    number_list.append(int(number))
    total_number = sum(number_list)
print(total_number)