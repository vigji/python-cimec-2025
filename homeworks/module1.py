# %%
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
# works to isolate the neurons (they will appear as some 15-20 blobs in the image).
# You can plot the boolean mask using matplotlib to see how it looks like.

wlims = [0, 20]




folder = Path("/Users/vigji/Downloads/Animal 1_Day 7")

# list all files in the folder
files = sorted(list(folder.glob("*.tif")))

# load first 350 tiffs into a 3D array
imgs = np.stack([np.array(Image.open(f)) for f in files[:250]])
imgs = imgs[:, 50:-50, 50:-50]
mean_proj = np.mean(imgs, axis=0)
# %%
# save the array to a file
np.save("/Users/vigji/code/python-cimec-2025/practicals/data/calcium_data.npy",  imgs)
# %%
plt.imshow(mean_proj)
# plt.plot(np.mean(imgs[], axis=(1,2)))







plt.figure()
#plt.imshow(mean_proj[hlims[0]:hlims[1], wlims[0]:wlims[1]])
plt.plot(np.mean(imgs[:, hlims[0]:hlims[1], wlims[0]:wlims[1]], axis=(1,2)))

# %%
dff = (imgs - np.mean(imgs, axis=0)) / np.mean(imgs, axis=0)

# %%
plt.figure()
plt.plot(np.mean(dff[:, hlims[0]:hlims[1], wlims[0]:wlims[1]], axis=(1,2)))
# %%
