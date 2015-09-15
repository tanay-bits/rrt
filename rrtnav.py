import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as mp
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy.spatial.distance import euclidean

def connect(p1, p2):	
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]

	xpixels = []
	ypixels = []

	for x in range(x1+1, x2):
		xpixels.append(x)

	for y in range(y1+1, y2):
		ypixels.append(y)

	pixels = zip(xpixels, ypixels)
	return pixels



FNAME = "N_map.png"

world = imread(FNAME)
world = np.flipud(world)
Xmax = world.shape[0]
Ymax = world.shape[1]
mp.hold()
mp.imshow(world, cmap=mp.cm.binary, interpolation='nearest', origin='lower',
              extent=[0,Xmax,0,Ymax])
# mp.show()



K = 390
verts = [[40, 40]]
goal = (60, 60)
edges = []

for i in range(K):
	rx = np.random.randint(0, 100)
	ry = np.random.randint(0, 100)		

	oldDistance = 10000

	for v in verts:

		pixels = connect((v), (rx, ry))
		for (x, y) in pixels:
			if world[x][y]:
				continue

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

# fig = mp.figure()
fig = mp.gcf()
path = Path(points, codes)
patch = patches.PathPatch(path)
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim([0,100])
ax.set_ylim([0,100])
mp.show()
