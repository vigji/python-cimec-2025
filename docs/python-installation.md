# A clean Python installation using `conda`
_(as of May 2025)_

It is finally the moment to move from the safe harbours of Google Colab into the perilous waters of local Python installations! 

For now follow the instructions below - but don't be scared, it will all make sense in the end!

**Note:** a _local Python installation_ means a Python interpreter running Python instructions on the CPU of your computer (this is different from running Python instructions on a remote server, which is what we have been doing with Google Colab)

## Before you start
Do you actually need a new Python installation? Pick the option that best describes you:

- _I have never used Python on my computer before_: you need a new Python installation. Continue to `Python installation`
- _I remember doing something with this Python thing a while ago on my computer, but I don't remember what._
    
    We'll need more information:
  - _I installed Anaconda a while back and never used it again_: you probably want to uninstall it and start from scratch. To uninstall it, follow the instructions [here](https://docs.anaconda.com/anaconda/install/uninstall/). 
  - _I used Python to run some important code which I might need again_: Contact us, we'll figure out what to do to keep your stuff running.
  - _I installed Python but not through Anaconda_: contact us, we'll figure out what to do to remove it
  
- _I have a Python installation on my computer, and I know the basics of how to run it locally_: you can skip this installation. Just make sure you have the following packages installed for now:
  - `numpy`
  - `scipy`
  - `matplotlib`
  - `pandas`
  - `scikit-learn`
  
  And that you can run Jupyter notebooks.

---

## Python installation
We will be managing our local Python installation using `conda`. `conda` is a package manager, which means it is a program that will help you install and update Python and its libraries. It is also a virtual environment manager, which means it will help you create and manage different Python environments - more on this in the next lecture!

### 0. Download and install (Mini)`conda`
Go [here](https://www.anaconda.com/download) and download the latest **Miniconda** installer for your operating system.

After the download, run the installer and follow the instructions. The only option I recommend checking and changing if needed is the installation path. I recommend installing `conda` in your home directory, so that it is easy to find and manage. Make sure it is directly under  `/Users/your-username/` (Mac) or `C:\Users\your-username\` (Windows).

#### Test your `conda` installation
Open a terminal (Mac; you can search it with the OS search) or an Anaconda prompt (Windows; you can search it with the OS search) and type `conda`. If you see a list of commands, you are good to go! If you get something like `conda: command not found`, ask us for help!

---
### 1. Install Jupyter in the base environment
We will install Jupyter in the base conda environment so it can be used with any Python environment we create. In your terminal, make sure you're in the base environment (if you see `(base)` at the start of your prompt, you are), then run:

```bash
conda install -c conda-forge jupyterlab
```

This will install Jupyter and all its dependencies in the base environment. If you are asked to confirm the installation, type `y` and press enter.

#### Test your Jupyter installation
Type the following command in the terminal:

```bash
jupyter lab
```

You should see a browser opening with a Jupyter notebook interface. If you get something like `jupyter: command not found`, you might want to close the terminal and open it again. If the problem persists, ask for help!

**Note**: After you open a notebook, you won't be able to work on the terminal you have launched it from! For the following steps, first close the notebook! (by first closing the webpage, then pressing `Ctrl+C` on the terminal).

---
### 2. Create a new Python environment
We will now create a new Python environment. This is a good practice to keep your Python installations clean and tidy.

From the terminal you opened for testing, write the following command:

```bash
conda create -n course-env python=3.11
```

This will create a new Python environment called `course-env` and install Python 3.11 in it. 

#### Test your new environment
To activate your new environment, and check that it is working, type the following commands:

```bash
conda activate course-env
python --version
```

This should print `Python 3.11.something`. If it doesn't, ask for help!

---

### 3. Install the packages we need
We will now install the packages we need for the course. In the terminal with your activated environment, copy the following commands:

```bash
conda install -c conda-forge numpy scipy matplotlib pandas scikit-learn scikit-image ipykernel
```

This will install all the necessary packages from the conda-forge channel, which is generally more up-to-date and better maintained than the default channel.

#### Test your packages
First, make sure your environment is properly registered as a Jupyter kernel:

```bash
python -m ipykernel install --user --name=course-env --display-name="Python (course-env)"
```

Then, from any terminal (since Jupyter is installed in base), type:

```bash 
jupyter lab
```

Click on the `New` menu and check that you see `course-env` in the list of available kernels. If you don't see it, try running the kernel installation command again.

Select `course-env` and create a new notebook. In the first cell, type the following code:

```python
import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.random.randn(100))
plt.show()
```

And check that a plot pops up. If it does not, ask us for help!

---
