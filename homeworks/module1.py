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

img = fetch_image()  # print its shape to know the number of pixels


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