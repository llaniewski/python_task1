import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as colors
import numpy as np

import matrix

out = "output.txt"
infile ='input.png'

img = mpimg.imread(infile)

nsize = 20

nonreduced = np.copy(img)

R = matrix.reduce( img[:, :, 0], (nsize, nsize))
G = matrix.reduce( img[:, :, 1], (nsize, nsize))
B = matrix.reduce( img[:, :, 2], (nsize, nsize))

# old fashion
# img = np.array( [ [ [R[i][j], G[i][j], B[i][j]] for j in range(nsize)] for i in range(nsize)] )
# or
img = np.zeros((nsize, nsize, 3))
img[:, :, 0] = R
img[:, :, 1] = G
img[:, :, 2] = B


hsvimg = colors.rgb_to_hsv(img)
hsvimg[:, :, 1] = 0

cliped = np.copy(hsvimg)

# old fashion
# dark = np.array( [ [ [False] for j in range(nsize) ] for i in range(nsize)] )
# light = np.array( [ [ [False] for j in range(nsize) ] for i in range(nsize)] )
# or
dark = np.zeros((nsize, nsize), dtype=bool)
light = np.copy(dark)

for i in range(nsize):
    for j in range(nsize):
        if hsvimg[i, j, 2] < 0.3:
            cliped[i, j, 2] = 0
            dark[i, j] = True
        elif hsvimg[i, j][2] < 0.6:
            cliped[i, j][2] = .3
            light[i, j] = True
        else:
            cliped[i, j, 2] = 1


with open(out, 'w') as f:
    for d, l in zip(dark, light):
        line = np.array(["  "]*nsize)
        line[d] = "||"
        line[l] = "- "
        f.write("".join(line))
        f.write("\n")