# Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axis
# Author: Brendan Tunney

# Import numpy & matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Setting X-Axis range

xpoints = np.array(range(0,4))

#Setting Y-Axis range

ypoints = (xpoints)
ypoints2 = (xpoints*xpoints)
ypoints3 = (xpoints*xpoints*xpoints)

#Plotting graph along with labels & line colour

plt.plot(xpoints, ypoints, label= "X", color = "Black")
plt.plot(xpoints, ypoints2, label= "X-Squared", color = "Green")
plt.plot(xpoints, ypoints3, label= "X-Cubed", color = "Red")
plt.legend()


#Saving file

plt.savefig ("Plot Task.png")

plt.show()

#References - W3 Schools & Lecture material