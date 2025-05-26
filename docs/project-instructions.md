# Submission of final project

The final assignment of the course consists in a small Python project, ideally something that could be useful for your work or some extra-curricular endeavior.  If you have already some half-backed or questionably written project going on, expanding and refactoring would also be suitable ideas! Look below for ideas and examples from last year.

The deadline for the submission is **Friday, the 29th of August 2025**! While you work on the project, feel free to ask for feedback at any point.

### Format
The project should be **uploaded to a public repository in your GitHub**, named `python-cimec-name-surname`. A link to the repository will be the only accepted submission form! If you have concerns about leaving it open, let us know and we can discuss it. 

> **:warning: Important :warning:**
> 
> You must demonstrate understanding of basic Git operations:
> 1. Creating a repository
> 2. Cloning it to your computer 
> 3. Adding files, committing changes, and pushing to GitHub
>
> Files uploaded directly through GitHub's web interface (like uploading to Google Drive) will not be accepted (GitHub tracks how files were added to the repository).


### Project content
Depending on the project, it could consist of one or more notebooks, and/or (encouraged) functions and classes defined in separate `.py` modules.

Make sure you **thoroughly document your code**! Try to write self-explanatory code (meaningful variables names, logical flow...) and add comments where you feel necessary. It shouldn't just work, it should be readable! Take the chance to try doing that well, as you will get feedback about it! If you write notebooks, make sure you use the markdown cells to describe the notebook content and to add all the required explanations to the analysis flow.

### `README.md`
The project **must** feature a `README.md` in the repository with a (schematic) description of the project aims and structure.
Ideally, after a brief description, in the `README.md` you should give some instructions about how to install and run the code. If you want, you can find [here](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf) a markdown cheatsheet. For some random examples see [here](https://github.com/AlliedToasters/circle-fit), or [here](https://github.com/portugueslab/xiao_et_al]) for the descriptions of different kinds of projects).

### Examples 
To give an idea, reasonable projects could be like:
 - Preliminary analysis of a dataset (with data loading, aggregation, plots...); either original data or from the web
 - Implementing a new experiment / preparing the material to run an experiment (eg images for a stimulus)
 - Refactoring some old code you wrote before (conceptual and not only cosmetic! Avoiding duplicated code, reusability, etc.). If you go this way, it would be great to share code before and after refactoring!
 
Random examples from past years course:
 - EEG data analysis pipeline[link](https://github.com/InesSeverino2/python-cimec-ines-severino)
 - A simple neural network for image detection [link](https://github.com/matteo-d-m/python-course-cimec-2023)
 - Analysis of questionnaire data using `pandas` [link](https://github.com/Deb-spg/final_assignment_python_cimec)
 - Workflow refactoring using `pandas` [link](https://github.com/pepstub/project-python_course2023/tree/main)
 - Analysis of behavioral data [link](https://github.com/samsrtn/Final_Python_Project_Sartin)


## Important: On the use of LLM-assisted coding

I am a big fan of LLM- assisted coding (and do that a lot myself); but I also find that for beginners it is very detrimental to understanding what is going on. My general idea is:

- If you start from a reasonable level of coding, feel free to use GPT/Claude/Cursor/Copilot as much as you want; but I'd say, use it to really step up your game. If you go this way, I expect your project to be significantly developed: a full analysis or experimental flow, nicely compartimentalized code, ideally class-based, etc.

- If you are a beginner, you should not use GPT for more than "I don't remember how to sort a dictionary" or "I don't remember how to plot a histogram". If you want to present a "beginner" project, please keep it t least 80% GPT-free.

Consider that it is quite straightforward to tell which parts of code are GPT-generated for beginner/mid-level programmers. I have been very indulgent for homework, I will not be here as I want to get the sense of how far you can go on your legs by the end of the course! 

I won't fail you either. So please, if you are a beginner, just keep to project super-easy ("I read this data from my pc in dataframes, computed some stats, and plotted a histogram") but do it yourself!