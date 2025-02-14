---
title: "Python for Open Neuroscience"
subtitle: "Pre-course"
author: "Luigi Petrucco"
theme: "metropolis"
date: "2025-02-07"
aspectratio: "169"
---

# Outlook

 - What is a computer? What is it good for?
 - The language of computers
 - How to make computers do things for you

# Before starting...

 - This lecture is super experimental! Please interrupt at any time, and let me know if you think I'm talking bullshit :)


# First of all...

 - What is a computer?


# From Wikipedia:

 > A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation).

# In other words:

 > A machine that can think for you...

# In other words:

 > ...if you ask politely!

# Dull tools

 - Many times, we use computers without really having them do stuff for us:
   - reading documents
   - writing documents
   - checking a calendar
   - looking at pictures
   - ...

# Dull tools

 (Of course, there are a lot of computery things happening under the hood. But they are not what we actually care about!)


# Fast tools

 - Some other times, we do leverage quick operations that they can do:
   - searching through files
   - suggesting contents
   - ...

# Turing completeness

 - The super cool thing about computers is that *in principle* they can do _anything_ you can do with your brain*
 
 *Warning: endless philosophical debates are still ongoing here

# Writing programs

 - Usually, we use a computer in ways that were designed by someone else
 - To turn a computer into a really useful thing, we want to _learn how to ask it to do things that nobody asked before_
 - Basically, we want to avoid click things and write stuff!

# Writing programs

 - To do this, we want to learn how to _write a program_
 - Programs: a sequence of instructions that the computer can follow to do stuff

# Why writing programs can be hard?

 - talking to computers is basically just like talking to a child...

# Why writing programs can be hard?

 - who does not understand your language...

# Why writing programs can be hard?

 - ...and by the way is foundamentally a toaster

# Binary storage

 - Everything the computer operates on must be "physically represented" somewhere in the computer
 - This happens by having a _lot_ of tiny "light bulbs" that can be turned on and off within the memory of the computer
 - Each light bulb can be in one of two states: on or off
 - We can use these light bulbs to store numbers using _binary code_

# Binary arithmetic

 - In binary, we only have two digits: 0 and 1
 - In binary, we can only count with 1s and 0s: 0, 1, 10, 11, 100, 101, 110, 111, 1000, etc.

# Translating to binary

 - Any kind of data has to be converted:
    - 1. To a finite sequence of numbers
    - 2. To a sequence of 0s and 1s, so that our hardware can store it


# Example: text

 - To represent a text, we have to:
    1. Split it in a sequence of characters
    2. Convert each character to a number
    3. Store the numbers, for all characters, in a binary format

# Question

How many letters we can write with 1 byte?

# Example: images

 - To represent an image, we have to:
    1. Split it in a grid of pixels
    2. For each pixel, find the intensity of the light for different color channels
    3. Convert each intensity to a number
    4. Store the numbers, for all colors and for all pixels, in a binary format

# Question

How many colors we can represent with 1 byte?

# File formats

In your computer, you store data in many different formats. Each file ultimetely consists just of 0s and 1s, and its format tells you how to interpret that sequence!

 - Corollary: most file types can be read one way or another, given a flexible enough tool! (eg Python)


# Computer programs

# Noise debugging
:::: {.columns}
::: {.column width=50%}
 - No noise with anaesthetized animals
 - maybe not motor artefacts, but maybe issue with shorting animal with setup ground?
:::

::: {.column width=50%}
![Noise](imgs/20250131/noise.jpg)
:::
::::