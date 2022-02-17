# Build-a-graph
This was my first big python projet. My goal was to practice a lot of the fundementals and try and incorporate that into data science through the use of MatPlotLib. There were a lot of hurdles I had to overcome with this, but it helped me learn a lot going forward.

## Challenges

### Repeating a question till the user enters a valid answer.
This was difficult for me to do. I would start with an if else statement, but I wanted it to repeat the question again till the input was satisfied. So, I started using while loops. Specifically, I had to use While True:
>While True: was my saving grace

Basically every question I asked the user for I would use something along this format:
![While True](https://user-images.githubusercontent.com/99676174/154581372-c2f5fb87-5f46-4ea0-bcf7-c9323fdfb660.PNG)

In this case, if the user said no, I wanted the program to end. Intially, it just accepted the 'n' input and then would break out of the while loop. So i had to import sys and then run the sys.exit() command.

Another big thing was the use of continue to repeat the while loop and break to leave it. That paired with If Else statements allowed me to solve most of the errors.

### Recieving X variable and making it into a list
I didn't think this would be difficult, but I couldn't figure out how to take user input and convert it into a list. I found out on Stack Overflow that you can use the .split() function then run a for loop like I did below.
![X to int](https://user-images.githubusercontent.com/99676174/154582004-e53b34ba-475d-436f-a4e7-c2f1baf018be.PNG)

The .split() function would take all variables with a space and split them then the list would be made into a list of integers with the int(x[i]).

### ValueErrors
So at this point, I knew While loop allowed me to keep asking the user a question till they get it right, then if else statements to determine whether the while loop kept going (continue) or finished (break).
The next challenge was when the user would throw an error. This happened during the creation of X and Y variable.

![Y to int](https://user-images.githubusercontent.com/99676174/154582500-7812e1b1-5b55-4146-9b08-433333d06b5c.PNG)

This is the part I struggle with. I understand that the code is "trying" something and if it throws an error, it goes to the "except" statement. That way your code doesn't end. I guess the reason this throws an error the way I want is because if the for loop is unable to split the data as an integer, then then it would throw an error which the try except clause catches.

### Finding user errors
What I talked about above took care of most of the work. Now, I spent a lot of time just trying to make the code throw an error.
Basically, if they entered no data, wrong type, or didn't answer the question, I wanted it to be addressed. 

![color](https://user-images.githubusercontent.com/99676174/154583020-c04a902f-1302-46fa-bdda-ec4d61ee2be3.PNG)

In this section about colors, I made sure they choice from the list, actually entered something, and wasn't a number. Because if they entered something wrong, later down the road when the program tries to build the graph, it would throw an error.

## Closing thoughts
Overall, this was meant to be very simple, but I quickly realized that most of my battle would be making sure the user doesn't do something that would cause the program to stop. If someone entered everything in completely correct, this could be 25% the size.
>Basically, it felt like damage control

I am very satisfied and proud of what I did by myself for this first project!

