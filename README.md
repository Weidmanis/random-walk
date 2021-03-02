# Random-walk Visualiation 

## Three programms:

Maths, history and further reading on Random Walk:
[Random_walk](https://en.wikipedia.org/wiki/Random_walk)

# 1. Random Walk in 1D

* Simple function generates a list of numbers that are based on the previous value plus the step that is picked at random
* Using matplotlib it is then simply plotted
* Once can change step count in the for loop to increase/decrease the length of the walk

# 2. Random Walk in 2D

* Now x and y coordinates are needed to plot a 2D graph
* NOTE: There are 9 (3x3) possible step sizes that can be taken when all combinations for x and y are considered
* Step sizes are left as [1,0,-1]
* At random x,y coordinates (step) is chosen and appended to the existing lists
* Turtle library is used to plot animated x,y coordinates


# 3. Random Walk in 3D

* x, y, z coordinates are generated using function
* There are 27 (3x3x3) steps that can be picked from for each iteration
* Again, at random step is picked and then added to x,y,z coordinate lists
* Lastly coordinates are plotted in a 3D plot using matplotlib