import configparser
import pandas as pd
import numpy as np
import os
import math
import time
import copy
import scipy as spB
import pydoc

import itertools
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import collections as mc
from matplotlib.patches import Ellipse, Polygon
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation
from matplotlib import animation
plt.style.use('seaborn-pastel')

lines = [[(0, 1), (1, 1)], [(0, 1), (0, 2)], [(0, 2), (1, 1)], [(1, 1), (1, 2)], [(1, 2), (0, 2)], [(1, 1), (1.5, 2.5)], [(1.5, 2.5), (0, 2)], [(0, 2), (0.75, 1.75)], [(0.75, 1.75), (1,1)],
                                [(0, 2), (0.25, 1.25)], [(0.25, 1.25), (1,1)]]
c = np.array([(0, 0, 0, 1), (0, 0, 0, 1), (0, 1, 0, 1), (1, 0, 0, 1), (1, 0, 0, 1), (0, 0, 1, 1), (0, 0, 1, 1)])

lc = mc.LineCollection(lines, colors=c, linewidths=2)
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)

plt.show()
