# Python for (open) Neuroscience  - 2025

<img align="right" width="400" height="400" src="https://imgs.xkcd.com/comics/python.png">

Python is an **open-source**, **high-level**, **multipurpose** programming language. It offers tools for fast **manipulation of large matrices** and datasets (similar to MATLAB) and **powerful data aggregation** and statistics (akin to R), together with thousands of packages for **machine learning**, **visualizations**, simulations, hardware control, and many others. As a result, **a growing number of labs are adopting it for their workflows**.

This course will start covering **the basics of Python usage** and build up from there to some **more advanced topics**. The aim is to bring participants up to speed in using **Python to solve some of the common problems** we face daily in the lab. People with some Python experience are welcome! You can assist other students in the first part, and then learn something new and useful in the later modules.


<br/><br/>
<br/><br/>

## Lectures recordings
- [Lecture 0.1](https://youtu.be/TMss3OOHrLE): Data structures (list, dict, tuple, set)
- [Lecture 0.2](https://youtu.be/34A9iWaIqvM): Flow controls (if/else, for loops)
- [Lecture 0.3](https://youtu.be/ZlN6qyjW488): while loops; functions

---

## Organization of the course

**Structure**: The course will be organized in four modules. Each module comprises three sessions, two hours each, that will mix frontal lectures and hands-on parts to work on. 
 
**Schedule**: the course will run every Monday (tentative time: 17:00-19:00) from February to June 2025. Dates are flexible and we can change them during the course if there's constraints/preferences on the student's side.
    

**Framework and requirements**: You will be following the course on your own laptop. The first two modules will be teaching using **Google Colab**, with **no installation required** (you will only need a browser and a working internet connection). In the second part we will move to **Jupyter Notebooks**, to understand how to **set up an real-world Python environment** that can be used in the every day research work. There won't be system requirements, we should be able to set it up on Windows, MacOS, and Linux (you will have instructions and assistance for doing that!).

**Assignments**: At the end of each of the first three modules there will be **a minimal recap assigment**, and a **time slot to ask questions** on the lectures and on the assignment. 

**Material**: The material will consist in jupyter notebooks and python scripts with the lecture content and exercises and it will be made available before the lectures using GitHub. 


## Syllabus
Syllabus for the course. Ideally, its incremental nature should ensure that each core concept that is introduced is then revisited and expanded on in every new lecture.

---


### Module 0: the fundamentals 🏗
A gentle introduction to the basic syntax and structure of Python code, just a smattering: more will come while exploring other modules.

 - **0.0. Introduction to Python variables and statements**: The very fundamentals of Python syntax; variable types (numbers, strings) and their operators.
 - **0.1. Data structures and flow controls**: data structures (lists, dictionaries, tuples, sets),
 - 
 - **[planned] 0.2. More flow control, and style**: basic clauses (`if`/`elif`/`else`, `while`/`for`  loops), first notes on style; jupyter notebook tricks; `break`, `continue`,
 - **[planned] 0.3. Flow control, functions (and modules ?)**: `try`/`except`; packing code in a function
 - **[planned] 0.4. Fundamentals of classes and objects**: Definition of classes and their components (methods, attributes, properties); using classes and reading their docs
 - **[planned] 0.5. Creating new classes**: how can we create a new class; practical examples of classes for data loading

**Assignment**: Exercises tba

---


### Module 1: the scientific stack in Python 📚
We introduce the Holy Trinity of data analysis: `numpy`, `pandas`, and `matplotlib`; and we show how they solve almost all our data analysis problems.

 - **[planned] 1.0. `numpy` and `matplotlib`**: Data types: the `np.array`. initialisation, operators, indexing (numerical and boolean masking); operations with arrays (concatenate, stack, searching extrema, sorting, using sorting indexes). Visualising arrays and matrices with `matplotlib`. Reading and writing `.npy` files.
 - **[planned] 1.1. `pandas`**: `pd.Series` and `pd.DataFrames`; reading and writing `.csv` files. Optimal ways to organize data in dataframes. Working with dataframes: indexing, slicing, selecting, querying, interpolating, mapping. Using `matplotlib` to visualise datasets. 

**Assignment**: Exercise tba

---


### Module 2: Real-world Python for real-world data 🔬
We start using all of the above on some real world scenario and neuroscientific data, trying to find common solutions to problems and tasks from different fields.

- **[planned] 2.0. Real-world Python for real-world data**  Moving from Google Colab from local Python (using Anaconda) and jupyter notebook; understand where things are in a local installation; install new modules with `pip`.
 - **[planned] 2.1. Working with local files: Interact with local data: browse and reorganize folders; opening or importing the most common data types that might come from experiments (`.txt`, `.csv`, `.xlsx`, `.mat`, `.tiff`, ...to adjust depending on interest).
- **[planned] 2.2. More on `pandas`** Advanced `pandas`: aggregated operations using `groupby()` and `rolling()`. Group statistics, smoothing, resampling. Mindblowing `pandas` (depending on progress/interest): hierarchical indexing with `MultiIndex`, aggregated operations, dataset alignment. Introduction to `seaborn` for dataset visualization.


**Assignment**: Exercise tba

---

### Module 3: Advanced topics in Python for neuroscience ☄️
We see how to bring home the bacon with Python as neuroscientists. Keep your code organised, generate good paper figures, make sure that your code is documented and accessible. Here are some possible topics, but we will choose together and pick up three based on interest.

Here are some options:
- **Advanced visualisation and data rendering** Some basic concepts and rules of data visualisation using `matplotlib`, tips for generating paper quality figures. More on `pandas` and `seaborn`. How to create animations with `matplotlib` and `napari`.
- **Version control using `git` and GitHub** Advantages and importance of version control systems. Core `git` concepts: `add`, `commit`, `branch`. Synch code with GitHub: `fetch`, `pull`, `push`.
- **Organising and publishing scientific code.** Best practices for clean and readable scripts and notebooks. Design principles for a data processing pipeline; structure of a pip installable repository. How and where to deposit code for a publication.
- **Scripting experiments using Python** Use Python to generate visual or auditory stimuli. Brief introduction to Psychopy. Interacting with Arduino and NI boards to read and write digital, analog and serial inputs/outputs
- **Fundamentals of statistics and machine learning with Python** Compute basic statistical tests with `scipy.statistics`. The `scikit-learn` package: Dimensionality reduction and clustering. Using Principal Component Analysis (PCA) to reduce dimensionality on a dataset. Introduction to clustering using the K-means algorithm
- **...**


**Assignment**: You will be ask to complete a small Python project of your choice addressing a problem from your daily work at the lab. Could be anything: count cells from images, perform some data analysis on existing datasets, visualize EEG timeseries or MRI stacks, hack the institute coffee machine card...

---


### Complimentary soft skills
Ideally, the course will also try to convey some more elusive coding-related soft skills, such as:
- **Write good data analysis code**, keeping an eye on reusability, readability, parameterisation... 
- **Learn how not to get stuck** and learn from bugs: find online resources (documentation, StackOverflow, GitHub); and interact with them (asking questions, reporting bugs, raising issues, etc.)
- **Understand the value of open source code** in the scientific endeaviour, and the importance of depositing code and datasets.

## Additional online resources and exercises
#### Intro level
Those is mostly aimed at people who have never written a line of Python, or have forgot everything about it.

- [Datacamp](https://www.datacamp.com/courses/intro-to-python-for-data-science): requires registration, but offers free intro courses for basic Python usage. Very boring, as drills should be.
- [Codecademy](https://www.codecademy.com/learn/learn-python-3): has same formula, with free account offers some basic Python tutorials.
- [Udacity](http://udacity.com/course/cs101): again the same, more based on videos.


#### Intermediate level

- [Python for neuroscientists](https://pyforneuro.com/)
- [Case Studies in Neural Data Analysis](https://mark-kramer.github.io/Case-Studies-Python/intro.html)
- [Computational Neuroscience in Python textbook](https://mrgreene09.github.io/computational-neuroscience-textbook/)




