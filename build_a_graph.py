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

# Color selection
col_choice = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']
print("\nChoice from the list below a color for your graph: ")
for col in col_choice:
    print(col)
while True:
    color = str(input('\nWhat color do you want the data to be?: '))
    if color.isdigit():
        print('That is a number. I need a color')
        continue
    elif color == '':
        print("GIVE ME A COLOR!!")
        continue
    elif color.lower() in col_choice:
        break
    else:
        print('That is not on the color list!')
        continue
        
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
