#############
# Lecture 0.0
#############

# 0.0.0
# Create a variable that checks if a year is a leap year
# A year is a leap year if it's:
# - divisible by 4 AND
# - not divisible by 100, unless it's also divisible by 400 (eg 1700 is not a leap year, 1600 is)
# Test the results with the following years:
year_0 = 1900
year_1 = 2000
year_2 = 2024
year_3 = 2025

year_to_test = year_0  # change this to test other years

is_leap_year = ...



# 0.0.1
# Create a temperature converter that:
# 1. Takes a temperature in Fahrenheit (use float)
# 2. Converts it to Celsius (google the formula)
# transforming the float result into an int
# 3. Define variables telling you if water would:
#    - freeze (below 0°C)
#    - boil (100°C or above)
#    - or be liquid (between 0-100°C)
# Test with these temperatures:
temp_0 = 32.0    
temp_1 = 212.0   
temp_2 = 98.6    
temp_3 = -40.0

temp_to_test = temp_0  # change this assigment to test other temperatures

temp_in_celsius = ...  # make sure this is an int!
is_frozen = ...
is_boiling = ...
is_liquid = ...   # ensure that only one of these is true for each of the possible temperatures!


#############
# Lecture 0.1
#############

# 0.1.0
# Create a variable that stores the string "Hello, world!"
# Assign to a new variable the uppercase version of the string
# Assign to new variables the even and odd characters of the string
# Concatenate the even and odd characters together, separated by a space
# Print the result

stupid_text = "Hello, world!"

uppercase_string = ...
even_characters = ...
odd_characters = ...
concatenated_string = ...

print(concatenated_string)

# 0.1.1
# Choose what would be the best data structure to store the following data, and why; there can be multiple good answers
# 1. Names of all the students in a class, with the option to add or remove students
# 2. Address for every student in a list
# 3. x, y pair of coordinates for a point we need to plot
# 4. The group of *unique* IPs addresses accessing a server

# 0.1.2
# From the list below, pop the last element, and add it to the dictionary defined below, 
# under the key "new_element". Then, add the rest of the list to the dictionary,
# under the key "rest_of_the_list".
list_of_elements = [1, 2, 3, 4, 5]

dictionary_of_elements = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# Then index the first element of the "rest_of_the_list" list entry in the dictionary


# 0.2.0
# Text Analysis with Sets and Dictionaries
# In this exercise, you'll analyze two text samples to find patterns and differences.

text_sample1 = """
Python is a high-level, general-purpose programming language. Its design philosophy 
emphasizes code readability with the use of significant indentation. Python is dynamically 
typed and garbage-collected. It supports multiple programming paradigms, including structured, 
object-oriented, and functional programming.
"""

text_sample2 = """
Python is widely used in artificial intelligence, data analysis, scientific computing, 
and web development. Its syntax allows programmers to express concepts in fewer lines 
of code than would be possible in languages such as C++ or Java. The language provides 
constructs intended to enable clear programs on both small and large scales.
"""

# 1. Clean the texts by converting it to lowercase 
# (if you want you can also remove punctuation using string method replace())

cleaned_text1 = ...
cleaned_text2 = ...

# 2. Create sets of unique words for each text 
unique_words1 = ...
unique_words2 = ...

# 3. Find words that appear in both texts
common_words = ...

# 4. Find words that are unique to each text
only_in_text1 = ...
only_in_text2 = ...

# 5. Create a dictionary that maps each word to its frequency in both texts combined
# The dictionary should have the format: {"word": count}
# Think about how you could do the counting using a loop and a conditional statement
word_frequency = {}

# 6. Find the most common word across texts
# Hint: you can either find the way to sort the dictionary, 
# or use a loop and a conditional statement to find the word with the highest count:
top_five_words = ...






