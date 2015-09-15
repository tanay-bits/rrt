import numpy as np
import matplotlib.pyplot as mp
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy.spatial.distance import euclidean

K = 390
verts = [[49, 49]]
edges = []

for i in range(K):
	rx = np.random.randint(0, 100)
	ry = np.random.randint(0, 100)		

	oldDistance = 10000

	for v in verts:
		distance = euclidean((v), (rx, ry))
		#print distance
		
		if distance < oldDistance:
			qnear = v
			oldDistance = distance

	verts = verts + [[rx, ry]]

	edges.append([qnear, [rx, ry]])


points = []
codes = []

for j, k in edges:
    points.append(j)
    points.append(k)
    
    codes.append(Path.MOVETO)
    codes.append(Path.LINETO)

fig = mp.figure()
path = Path(points, codes)
patch = patches.PathPatch(path)
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim([0,100])
ax.set_ylim([0,100])
mp.show()