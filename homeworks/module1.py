# %%
#############
# Lecture 1.0
#############

# 0.1.0
# Images are just arrays! This is one of the reasons working with arrays is so important!
# (Usually images are H x W x 3 arrays, with the third dimension storing the values
# for each of the RGB channels. Here the image will be grayscale, so we only have 2D - no colors!).

# Use the function below to download an image, and print the shape of the array to know the number of pixels.
# Then, use plt.matshow to visualize it.


def fetch_image():
    """Fetch exercise data from github repo.

    Returns:
        np.ndarray
            Array with the exercise data.

    """

    # You should never import stuff in a function! I'm doing it here
    # just to keep together all the code that you don't really need to read now.
    import numpy as np
    import requests
    from io import BytesIO

    # URL of the .npy file on GitHub:
    URL = "https://github.com/vigji/python-cimec/raw/main/practicals/data/corrupted_img.npy"

    response = requests.get(URL)

    return np.load(BytesIO(response.content))


# Tip 1: remember to import matplotlib.pyplot first - and give it an alias! ("import ... as ...")
# Tip 2: to make the image grayscale, you can pass the cmap="gray" argument to the matshow() function!

img = fetch_image()  # print its shape to know the number of pixels


# It looks like the image got corrupted with some noise!
# To understand the noise pattern, you can try to look closer to it.
# Zoom in the image: plot it again, but selecting a small region using indexing
# (e.g., img[10:80, 70:130])

# Can you understand what is going on? Can you think of an indexing strategy
# that would filter out the noise?
# Try to retrieve the uncorrupted image with an indexing operation, and plot it!

# (See below if you are really stuck!)


# ...


# ...


# Hint: it looks like one every two columns of pixels has weird values! You could try to keep only one column every two...


# 0.1.1
# As we mentioned, color images are just (w, h, 3) arrays where the third dimension correspond to color.
# Color is represented by triplets of numbers indicating the load over the Red, the Blue, and the Green axis.
# Let's make a colored version of the image, where the left side of the image appears red, the center blue,
# and the right green!
# To do so, initialize an empty (w,h,3) array and use indexing to fill with the image values the correct
# channels in different parts of the image. Bonus points: do it with a loop.
# After you have done it, consider this question: were you working inplace or on copies?


########################
# Lecture 1.1
########################

# 1.1.0
# Let's look at some real neurons! The following function will download some microscopy data
# from a calcium imaging experiment (data from https://data.mendeley.com/datasets/hjgtsmyyv5/1)
# Run the following cell to load the data:


def fetch_image():
    """Fetch exercise data from github repo."""

    import numpy as np
    import requests
    from io import BytesIO

    URL = "https://github.com/vigji/python-cimec-2025/raw/main/practicals/data/calcium_data.npy"

    return np.load(BytesIO(requests.get(URL).content))


#  The data is a 3D array: first dimension is time, second and third are space (height, width).
#  Each value in the array is the fluorescence level of the pixel.

# 1. Plot the first frame using plt.imshow. You'll see a lot of blobs, or doughnuts.
# These are the neurons! They are labelled with a fluorescent dye. When they activate,
# fluoresce in the cell increases.

# 2. Single frames will be noisy! Plot the mean of the first 100 frames!

# 3. Let's try to look at what neurons are more active. Compute the maximum projection
# over time to locate the cells with more activity!

# 4. Many times, we want to normalize the fluorescence levels over time to compare activity
# across pixels, independently of their absolute fluorescence levels.
# To do so, for every pixel, we can:
# - compute a baseline value; in our case, we can use the mean over time;
# - subtract for every timepoint the baseline value from the timepoint fluorescence;
# - divide the result by the baseline value.

# The normalized signal is called DeltaF / F:
# delta_f_f = (f - mean_f) / mean_f

# Use broadcasing  to compute delta_f_f from the stack, without using for loops!

# 6. Let's say we want to make a boolean mask for the neurons. One way of creating such mask
# can be to use a threshold to find the pixels whose maximum projection is above a certain value.
# Try to compute such mask, playing with the threshold value until you find a number that
# works to isolate the neurons (they will appear as some 10-20 blobs in the image).
# You can plot the boolean mask using matplotlib to see how it looks like.
# %%
# %%

########################
# Lecture 1.2
########################

# 1.2.0
# Let's say we want to look at the signal for all neurons we have located.
# To find neurons, we can start from the boolean mask we have computed in the previous exercise.
# Make sure you have selected a threshold that separates (most) blobs from each other, meaning
# that there is complete separation (no touching points) between the blobs for the neurons.

# After computing the mask, we can find the indices of the pixels belonging to the neurons
# by using the `np.argwhere` or the `np.nonzero` function. Do it!

# 1.2.1
# After selecting the neurons pixels (you should get an array of shape (N, 2) where N is the number of neurons pixels),
# compute the mean signal across all neurons pixels over time, and plot it.
# You will see a (noisy) signal with some actibity peaks.

# 1.2.2
# Set a threshold on the mean of the neurons, and use argwhere to find the indices of the peaks!
# You can try to find a way to visualize the indexes that you find on the activity plot to check if they make sense.

########################
# Lecture 1.3-4
########################

# Here, we will download the information about about thousands volumns available on Amazon. 
# Just a tiny fraction of Babel's books, but way more organized!

# We will also get a dataset of users writing reviews, and a dataset of reviews.

# 0. Using, pandas, read the .csv files from the following urls. The files contain the books, the ratings, and the user data.
# Explore a bit the content of each df:

users_df_url = "https://github.com/vigji/python-cimec-2024/raw/main/assignments/files/users.csv"
ratings_df_url = "https://github.com/vigji/python-cimec-2024/raw/main/assignments/files/ratings.csv"
books_df_url = "https://github.com/vigji/python-cimec-2024/raw/main/assignments/files/books.csv"

# 1. plot an histogram of all the ratings from all users, and another histogram with the age of the users.

# 2. Using the ratings dataframe, compute the average rating for each book, and count how many reviews each book had. Then:
#      - find out which book had the highest number of reviews.
#      - find out which book had the highest average rating - but include only books that have at least 100 reviews!
#      - Finally, look for the titles that correspond to those book codes (ISBNs are unique book codes).


# 3. Let's get even more specific! Let's find the preferences of users in specific countries and with different ages.
# Use the users DataFrame to select only italian users under 40 years old.
# Then, go back to the reviews dataframe and filter only reviews from those users. 
# Compute the average ratings (include only books that have at least 3 reviews) and sort the ISBNs by average rating. 
# Finally, find the books corresponding to each ISBN code to get which books got the best ratings in this coort of people!

# (Optional): from the users DataFrame generate a list of all the countries present in the dataset. 
# Then, find the highest rated book in each one of those countries.

########################
# Lecture 1.5
########################

# From the data above, make a multi-panel figure; in each panel, plot the histogram of the ages of the users for a country (either all countries or the first six for number of users). Make sure the plot is fully readable, with labelled axes and titles specofying the country for every plot

