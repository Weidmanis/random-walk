import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# y(t) = y(t-1) + e, where e = random int,

def get_y(y, y_):

    for i in range(1000):
        e = random.choice([-1,1])
        y += e
        y_.append(y)

    return y_

# Set the initial state
y = 0
y_ = []

fig, ax = plt.subplots()
plt.plot(get_y(y,y_))
plt.show()
