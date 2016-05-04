

def reduce(matIn, n_size):
    nx, ny = n_size
    sx = len(matIn)
    sy = len(matIn[0])

    if sx < nx or sy < ny:
        raise Exception("New size should be smaller then origin")

    nxs = sx / nx
    nys = sy / nx

    mat = [[0. for i in range(nx)] for j in range(ny)]

    for i in range(nx):
        for j in range(ny):
            x = int(i*nxs)
            y = int(j*nys)
            ids = 1
            s = matIn[x][y]
            for xi in range(-1, 2, 2):
                for yj in range(-1, 2, 2):
                    ii = x+xi
                    jj = y + yj
                    if 0 <= ii < sx and 0 <= jj < sy:
                        s += matIn[x+xi][y+yj]
                        ids += 1

            mat[i][j] = s/ids

    return mat


# m = [[float(i*j) for i in range(5)] for j in range(5)]
#
# print np.array(m)
#
# print np.array(reduce(m, (3, 3)))
