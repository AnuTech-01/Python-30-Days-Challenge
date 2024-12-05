#mtploting plotting

import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()

#Add labels to the x- and y-axis:

'''import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([110,115,120,125,130,135,140,145,150,155])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()'''
