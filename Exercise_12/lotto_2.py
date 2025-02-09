import random
# Random module generates random variables
# Generate 6 unique random numbers using set to avoid duplicates
# used set method to define variable so numbers are printed as a set
lottery_numbers = set()
# Create a while loop for as long as the length of the lottery numbers are less than 6
while len(lottery_numbers) < 6:
# used add method to add numbers into the set between 1-50, also used method from random module which is random integer to get random numbers
 lottery_numbers.add(random.randint(1, 50))
# generate any number between 1 and 50
# Display the sorted numbers
# sorted function will display the numbers in numerical order
print("Your lottery numbers are:", sorted(lottery_numbers))

# simplified method
# using random.sample method to gain random numbers between a range of 1-50 and getting python to print it 6 times
lottery_numbers = random.sample(range(1,50),6)
print("Your lottery numbers are:", sorted(lottery_numbers))