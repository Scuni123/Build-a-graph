# Build-a-graph
This was my first big python projet. My goal was to practice a lot of the fundementals and try and incorporate that into data science through the use of MatPlotLib. There were a lot of hurdles I had to overcome with this, but it helped me learn a lot going forward.

## Challenges

### Repeating a question till the user enters a valid answer.
This was difficult for me to do. I would start with an if else statement, but I wanted it to repeat the question again till the input was satisfied. So, I started using while loops. Specifically, I had to use While True:
>While True: was my saving grace

Basically every question I asked the user for I would use something along this format:
```
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
```

In this case, if the user said no, I wanted the program to end. Intially, it just accepted the 'n' input and then would break out of the while loop. So i had to import sys and then run the sys.exit() command.

Another big thing was the use of continue to repeat the while loop and break to leave it. That paired with If Else statements allowed me to solve most of the errors.

### Recieving X variable and making it into a list
I didn't think this would be difficult, but I couldn't figure out how to take user input and convert it into a list. I found out on Stack Overflow that you can use the .split() function then run a for loop like I did below.
```
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
```
The .split() function would take all variables with a space and split them then the list would be made into a list of integers with the int(x[i]).

### ValueErrors
So at this point, I knew While loop allowed me to keep asking the user a question till they get it right, then if else statements to determine whether the while loop kept going (continue) or finished (break).
The next challenge was when the user would throw an error. This happened during the creation of X and Y variable.
```
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
```
This is the part I struggle with. I understand that the code is "trying" something and if it throws an error, it goes to the "except" statement. That way your code doesn't end. I guess the reason this throws an error the way I want is because if the for loop is unable to split the data as an integer, then then it would throw an error which the try except clause catches.

### Finding user errors
What I talked about above took care of most of the work. Now, I spent a lot of time just trying to make the code throw an error.
Basically, if they entered no data, wrong type, or didn't answer the question, I wanted it to be addressed. 
```
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
```        
In this section about colors, I made sure they choice from the list, actually entered something, and wasn't a number. Because if they entered something wrong, later down the road when the program tries to build the graph, it would throw an error.

## Closing thoughts
Overall, this was meant to be very simple, but I quickly realized that most of my battle would be making sure the user doesn't do something that would cause the program to stop. If someone entered everything in completely correct, this could be 25% the size.
>Basically, it felt like damage control

I am very satisfied and proud of what I did by myself for this first project!

