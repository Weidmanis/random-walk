import turtle
import random

turtle.speed('normal')

def random_walk(N):

    # Create two lists for x, y coordinates
    walkx, walky = [0], [0]

    for i in range(1 , N+1):

        # Choice of a step at random
        r = random.randint(0,8)
        
        # Possible steps
        steps = [
            [-1,-1],[-1,0],[-1,1],
            [0,-1], [0 ,0],[0,1],
            [1,-1], [1,0], [1,1],
        ]
        
        walkx.append(walkx[i-1] + (steps[r][0]))
        walky.append(walky[i-1] +(steps[r][1]))

    return [walkx, walky]

walk = random_walk(15000)

for x,y in zip(*walk):
    turtle.goto(x*10, y*10) # *10 = 10px