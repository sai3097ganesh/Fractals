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

num_cores = multiprocessing.cpu_count()
print(num_cores)

# if __name__ == "__main__":
#    processed_list = Parallel(n_jobs=num_cores)(delayed(my_function(i,parameters) 
#                                                        for i in inputs))

A = np.array([0,0])
B = np.array([1,0])
C = np.array([0.5, 1])

Starting_point = (A+B+C)/3

iterations = 5000

fig = plt.figure()
plt.axis([0, 1, 0, 1])

with writer.saving(fig, "writer_test3D.mp4", 100):
    for x in range(0,iterations):
        rand_value = random.randint(1,3)
        if rand_value == 1:
            Starting_point = (Starting_point + A)/2
        elif rand_value == 2:
            Starting_point = (Starting_point + B)/2
        elif rand_value == 3:
            Starting_point = (Starting_point + C)/2
        plt.plot(Starting_point[0], Starting_point[1], 'ro', markersize=2.5)
        plt.show()
        writer.grab_frame()