import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import multiprocessing
from joblib import Parallel, delayed
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=100, metadata=metadata)

x = 0
y = 0

iterations = 10000

fig = plt.figure()
plt.axis([-3, 3, 0, 10])

with writer.saving(fig, "writer_test3D.mp4", 100):
    for x in range(0,iterations):
        rand_value = random.randint(1,100)
        if rand_value == 1:
            x = 0
            y = 0.16 * y
        elif 2 <= rand_value <= 86:
            x = (0.85 * x) + (0.04 * y)
            y = (-0.04 * x) + (0.85 * y) + 1.6
        elif 87 <= rand_value <= 93:
            x = (0.2 * x) - (0.26 * y)
            y = (0.23 * x) + (0.22 * y) + 1.6
        elif 94<= rand_value <= 100:    
            x = (-0.15 * x) + (0.25 * y)
            y = (0.26 * x) + (0.24 * y) + 0.44
        plt.plot(x, y, 'go', markersize=2)
        writer.grab_frame()