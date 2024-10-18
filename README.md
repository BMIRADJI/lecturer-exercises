## a  program that asks auser to input and prints
          # all prime numbers less than to the input
          
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_less_than(n):
    print(f"Prime numbers less than {n}:")
    for num in range(2, n):
        if is_prime(num):
            print(num, end=' ')
    print()  # For a newline after printing all primes

# Input from user
user_input = int(input("Enter a number: "))
if user_input > 1:
    print_primes_less_than(user_input)
else:
    print("Please enter a number greater than 1.")
    
    
    
    
    
    
    
    
    
    
    
    ##program that reads from the keyboard a positive integer and displays in words
    
    
def number_to_words(num):
    """Convert a number into words."""
    if num < 0:
        return "Negative numbers are not supported."
    
    if num == 0:
        return "zero"
    
    # Define words for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    words = ""

    if num >= 1000:
        words += ones[num // 1000] + " thousand "
        num %= 1000

    if num >= 100:
        words += ones[num // 100] + " hundred "
        num %= 100

    if num >= 20:
        words += tens[num // 10] + " "
        num %= 10

    if num >= 10:
        words += teens[num - 10] + " "
    else:
        words += ones[num] + " "

    return words.strip()

# Input from user
user_input = input("Enter a positive integer: ")

try:
    user_input = int(user_input)
    if user_input > 0:
        print(number_to_words(user_input))
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter an integer.")

    
    
   
def remove_vowels(input_string):
    """Remove vowels from the input string."""
    vowels = "aeiouAEIOU"  # Define a string of vowels
    result = ""  # Initialize an empty result string

    for char in input_string:  # Loop through each character in the input string
        if char not in vowels:  # Check if the character is not a vowel
            result += char  # Add the character to the result if it's not a vowel

    return result  # Return the final result string

# Input from user
user_input = input("Enter a string: ")
output_string = remove_vowels(user_input)  # Call the function to remove vowels
print("String without vowels:", output_string)  # Display the result

          
          
         
          
def is_palindrome(input_string):
    """Check if the input string is a palindrome."""
    # Remove spaces and convert to lowercase
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Check if the string reads the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Input from user
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f'"{user_input}" true.')
else:
    print(f'"{user_input}" false.')
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root
        if num % i == 0:  # If divisible, it's not prime
            return False
    return True  # If not divisible by any number, it's prime

def display_primes_less_than(n):
    """Display all prime numbers less than n."""
    print(f"Prime numbers less than {n}:")
    for num in range(2, n):  # Start from 2 to n-1
        if is_prime(num):
            print(num, end=' ')  # Print prime numbers on the same line
    print()  # New line after printing all primes

# Input from user
user_input = int(input("Enter a positive integer: "))
if user_input > 1:  # Ensure the number is greater than 1
    display_primes_less_than(user_input)
else:
    print("Please enter a positive integer greater than 1.")


def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

# Input from user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')

##generate mean,mode,frequence

import random

def generate_random_numbers(count, lower, upper):
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_freq = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_freq]

    return modes if len(modes) == 1 else "No unique mode"

# Generate 100 random integers between 1 and 50
random_numbers = generate_random_numbers(100, 1, 50)

# Calculate mean, median, and mode
mean_value = calculate_mean(random_numbers)
median_value = calculate_median(random_numbers)
mode_value = calculate_mode(random_numbers)

# Display the results
print(f"Random Numbers: {random_numbers}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
