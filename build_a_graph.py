# ----------------------------------------------------------------------
# This is my first 'big' project in python.
# The whole purpose of this is to simply have the user give some input and then have a graph built.
# I wanted to try this to practice both my python skills and matplotlib skills.
# I am proud of this project since I did everything on my own (with the help of StackOverflow of course!)
# The biggest struggle was learning how to deal with user input errors. While True loops became very important.
# Try and Except loops were also crucial for errors.
# Learned a lot on this one. Hope you enjoy!
# -----------------------------------------------------------------------

import matplotlib.pyplot as plt
import sys

# starting Text
print("========================================="
      '==========================================')
print('========================================='
      '==========================================')
print("\nHi! This is my graph builder 3000. I'm going to ask a couple questions and then make you a graph based on your answers. ")

#Do you want to build a graph?
while True:
    start = input('Ready? y/n: ')
    if start.lower() == 'n':
        print(":( awe okay *cries*")
        sys.exit()
    elif start == '':
        print("Don't give me the silent treatment!")
        continue
    elif start.lower() == 'y':
        break
    else:
        print("what does that even mean?")
        continue

#Labels
title = input('\nGreat! What will your graph be called? ')
xlable = input('\nInteresting. Label the data found on the x axis: ')
ylabel = input('\nSame for the Y axis: ')

# X input to int
while True:
    x_input = input('\nEnter in some x value data separated by a space: ')
    try:
        x = x_input.split()
        for i in range(len(x)):
            x[i] = int(x[i])
        if x_input == '':
            print('You need to enter data!')
            continue
        else:
            break
    except ValueError:
        print("Sorry, I need numbers.")
        continue

# Y input to int
while True:
    y_input = input('\nEnter in Y data separated by a space: ')
    try:
        y = y_input.split()
        for i in range(len(y)):
            y[i] = int(y[i])
        if len(y) == len(x):
            break
        elif y_input == '':
            print("You need to enter data!")
            continue
        else:
            print("The number of Y points must equal the number of X points.")
            continue
    except ValueError:
        print("Sorry, I need numbers.")
        continue

# Color. This is probably not how you should do it, but it's all I could figure out. I know
# that is throws an error if you enter in a wrong color.
while True:
    color = str(input('\nWhat color do you want the data to be?: '))
    if color.isdigit():
        print('That is a number. I need a color')
        continue
    elif color == '':
        print("GIVE ME A COLOR!!")
        continue
    else:
        break

# Graph builder
while True:
    graph_type = input('\nDo you want a scatterplot or linegraph? s/l: ')
    if graph_type == '':
        print('Bruh I need a graph.')
        continue
    if graph_type.lower() in ('s', 'l'):
        break
    else:
        print("Sorry, I don't know that graph.")
        continue
if graph_type.lower() == 's':
    plt.scatter(x, y, color=color)
    plt.xlabel(xlable)
    plt.ylabel(ylabel)
    plt.title(title)
else:
    plt.plot(x, y, color=color)
    plt.xlabel(xlable)
    plt.ylabel(ylabel)
    plt.title(title)
plt.show()

print("\n\nI hope you liked your graph :)")
