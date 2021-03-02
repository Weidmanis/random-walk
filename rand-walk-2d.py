import turtle
import random

turtle.speed('slowest')

def random_walk(N):

    

    # Create two lists for x, y coordinates
    walkx, walky = [0], [0]

    for i in range(1 , N+1):

        r = random.randint(0,8)
        
        steps = [
            [-10,-10],[-10,0],[-10,10],
            [0,-10], [0 ,0],[0,10],
            [10,-10], [10,0], [10,10],
        ]
        
        walkx.append(walkx[i-1] + (steps[r][0]))
        walky.append(walky[i-1] +(steps[r][1]))

    return [walkx, walky]

walk = random_walk(15000)
print(walk)
for x,y in zip(*walk):
    turtle.goto(x*1, y*1)

