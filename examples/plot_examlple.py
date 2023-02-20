"""
This is my example script
=========================

This example doesn't do much, it just makes a simple plot
"""
# %%
# the project name is Plot Example
# --------------------------------

import matplotlib.pyplot as plt
from example import set_of_values

import numpy as np

x = set_of_values(1, 10)
y = np.ones(10)

# %%
# Draw the plot
plt.plot(x, y, "o", color="magenta")
plt.show()
