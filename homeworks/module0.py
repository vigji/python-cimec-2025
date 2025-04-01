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



# 0.3.0
# Create a function square_list that takes a list of numbers and returns a list of their squares
# (make sure you do not modify the original list!)

# Then, write a for loop to call it over numbers from 1 to 100 in lists of 10
# (first time between 1 and 10, then between 11 and 20, etc), and print "bingo" if the sum of the result list is a multiple of 3


# 0.3.1
# Encapsulate the Netflix session generator from the lecture
# inside a function that takes as arguments 
# all the parameters (probability, cliffhanger probability, etc.)
# and returns the number of watched episodes in a single session simulation.

# Define it in a way that the cliffhanger effect can be inactivated in
# the simulation if the cliffhanger_prob argument is set to None:


# 0.4.0
# You get the Counter class definition below. To understand how to use it, you can either:
# - peek at the code, or
# - use help(), dir(), ?Counter (remember the ? help query in jupyter notebooks), and other introspection tools

class Counter:
    """A simple counter class that can increment and reset.
    
    Initialize with Counter(start=0) to begin counting from a specific number.
    """
    def __init__(self, start=0, max_value=None):
        self._value = start
        self._increment_count = 0
        self._max_value = max_value
    
    def increment(self, step=1):
        """Increases counter by step (default 1) and returns new value"""
        self._value += step
        self._increment_count += 1
        if self._max_value is not None and self._value > self._max_value:
            raise ValueError("Counter value exceeds maximum value")
        return self._value
    
    def reset(self):
        """Resets counter to 0 and returns new value"""
        self._value = 0
        return self._value
    
    def __str__(self):
        return f"Counter(value={self._value})"


# 1. Create a Counter instance

# 2. Use a while loop to increment the counter by 2 until it exceeds 20 using the increment method 
# (you can check out the method definition, the docstring or ?Counter.increment to see the arguments)

# 3.Create a new Counter instance with a start value of 5 and a max value of 10

# 4. Increment the new counter by steps of 1 for 20 times using a for loop and the increment method. Can you do it?

# 5. Fix the above code by adding an if clause that resets the counter every 5 increments using the reset method.


# 0.5.0

# Create a class called RGBColor that can be used to represent colors in the RGB color space. 
# RGB colors are defined by three values for three different channels: red (R), green (G), and blue (B), 
# which can be integers between 0 and 255.

# 1. Initialize it with r, g, b values. Check that they are integers between 0-255, and set them to private attributes _r, _g, _b
# 2. Expose the r, g, b values as simple properties that just return the private attributes
# 3. Create a method called get_rgb_tuple that returns the r, g, b values as a tuple (r, g, b are stored in the private attributes _r, _g, _b)
# (optional: instead of a method, do this with a property named rgb_tuple)
# 4. Add a method called mix_with() that takes as input another RGBColor as argument,
#    and returns a new RGBColor with the average of the two colors' values over each R, G, and B channel (rounded to integers)

# This 4th step is a bit tricky, so here's increasingly explicit hints in case you are stuck!
# 1. You can access the r, g, b values of the other input color using its attributes/properties
# 2. you can loop over r, g, b of other_color and self to compute averages one channel at a time
# 3. You can use the three new (rounded with int()) averages to create a new RGBColor instance and return it