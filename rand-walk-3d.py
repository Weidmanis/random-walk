# 3d random walk
import random
import matplotlib.pyplot as plt

def rand_walk(N):

    # Starting point
    walkx, walky, walkz = [0], [0], [0]

    for i in range(1,N+1):

        #Number for random choice of a step
        r = random.randint(0,26)

        # possible step sizes (can play around with the step sizes)
        steps = [-2,2,0]

        choice = []

        # Generate nested list with possible steps
        for i in steps:
            for j in steps:
                for k in steps:
                    x = [i,j,k]
                    choice.append(x)

        # Add the coordinates to the lists for each axis
        walkx.append(walkx[i-1] + choice[r][0])
        walky.append(walky[i-1] + choice[r][1])
        walkz.append(walkz[i-1] + choice[r][2])

    return [walkx, walky, walkz]

res = rand_walk(10000)

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
# ax.grid(False)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.plot3D(res[0], res[1], res[2], 'red', alpha = 0.7)
plt.show()