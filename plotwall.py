# Plot wall

import numpy as np
import matplotlib.pyplot as plt

def limitwall(rc, zc, rlim, zuplim, zlowlim):
    nrc, nzc = np.array([]), np.array([])
    for i in range(len(rc)):
        if rlim <= 0 or rc[i] < rlim:
            if zuplim != 0 and zc[i] > zuplim: continue
            if zlowlim != 0 and zc[i] < zlowlim: continue

            nrc = np.append(nrc, rc[i])
            nzc = np.append(nzc, zc[i])

    return nrc, nzc

def rotateWall(rc, zc, angle=1):
    """ Rotate wall section around the symmetry axis """
    radAngle = angle * np.pi / 180
    nrc = rc * np.cos(radAngle)
    nyc =-rc * np.sin(radAngle) #here
    nzc = zc

    return nrc, nyc, nzc

def transformWall(rc, yc, zc, cameraPosition, cameraDirection):
    # [1] COMPUTE ROTATION MATRIX
    y = [0,1,0]
    v = np.cross(cameraDirection, y)
    c = np.dot(cameraDirection, y)

    vmat = [[0,-v[2],v[1]], [v[2],0,-v[0]], [-v[1],v[0],0]]
    R = np.add(np.identity(3), vmat)
    vmat2 = np.dot(vmat, vmat) * 1 / (1+c)
    R = np.add(R, vmat2)

    nrc = np.subtract(rc, cameraPosition[0])
    nyc = np.subtract(yc, cameraPosition[1])
    nzc = np.subtract(zc, cameraPosition[2])

    wallVector = np.dot(R, [nrc,nyc,nzc])

    return wallVector[0,:], wallVector[1,:], wallVector[2,:]

def plotwall(ax, wall, cameraPosition, cameraDirection, degreesStart=[0],
             degreesEnd=[360], rlim=0, zuplim=0, zlowlim=0, rmin=-1,
             rmax=1, zmin=-1, zmax=1, spacing=1, tiltAngle=0):
    rc = wall[0]
    zc = wall[1]
    plotstyle = 'w'
    linewidth = 0.5

    # Limit the wall to only inner parts
    rc, zc = limitwall(rc, zc, rlim, zuplim, zlowlim)

    n = len(rc)

    for i in range(len(degreesStart)):
        for degree in range(degreesStart[i], degreesEnd[i], spacing):
            # [1] ROTATE WALL SECTION AROUND ORIGO
            nrc, nyc, nzc = rotateWall(rc, zc, angle=degree)

            # [2] ROTATE AND TRANSLATE WALL SECTION AROUND CAMERA
            nrc, nyc, nzc = transformWall(nrc, nyc, nzc, cameraPosition, cameraDirection)
            wallVector = [nrc, nzc, nyc, np.ones((1,n))[0]]

            # [3] Apply camera matrix
            cameraMatrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0]]
            projectedVector = np.dot(cameraMatrix, wallVector)
            factor = np.divide(1, wallVector[2])
            factorMatrix = [factor,factor,factor]
            projectedVector = np.multiply(factorMatrix, projectedVector)

            # [4] Account for camera tilt
            r = projectedVector[0,:] * np.cos(tiltAngle) + projectedVector[1,:] * np.sin(tiltAngle)
            z =-projectedVector[0,:] * np.sin(tiltAngle) + projectedVector[1,:] * np.cos(tiltAngle)

            ax.plot(r, z, plotstyle, linewidth=linewidth)

