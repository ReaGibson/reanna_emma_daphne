# imported the random module
import random
# printing the module types in the console to be able to determine which is needed
#print(dir(random))

# created random_number variable to store the generated random number
# using the randint method to extract a random number between 1 and 50

random_number1 = random.randint(1, 50)
# prints the random number in the console, however only prints one
# repeated method with different variables for each number
#print(random_number1)
random_number2 = random.randint(1, 50)
#print(random_number2)
random_number3 = random.randint(1, 50)
#print(random_number3)
random_number4 = random.randint(1, 50)
#print(random_number4)
random_number5 = random.randint(1, 50)
#print(random_number5)
random_number6 = random.randint(1, 50)
#print(random_number6)

#created a variable to combine the numbers together
all_numbers = random_number1, random_number2, random_number3, random_number4, random_number5, random_number6
# used set method to get the numbers to present as a set
# needs to be a set as sets are unchangeable and does not allow duplicates
lotto_numbers = set(all_numbers)
# used an f string to add text on the console as well as the variable lotto_numbers
# to display the numbers
print(f'Lotto Numbers: {lotto_numbers}')

