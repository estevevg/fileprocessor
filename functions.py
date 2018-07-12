import matplotlib.pyplot as plt
import numpy as np

# Converts a file.txt from specified data to a matrix
def fileTxt2Matrix(file_path):
    ret = []
    started = False
    with open(file_path, "r") as fs:
        for line in fs:
            if started:
                data = line.split('\t')
                time = float(data[0])
                ampl = float(data[1])
                ret.append([time, ampl])
            elif 'Time	Ampl' in line:
                started = True
    return np.asmatrix(ret)

# Prints the matrix
def plotMatrix(mat, file_name):
    arr = file_name.split("/")
    name = arr[len(arr)-1]
    plt.plot(mat['matrix'][:, 0], mat['matrix'][:, 1])
    plt.title(name)
    plt.ylabel('Ampl')
    plt.xlabel('Time')

    plt.show()

def doExercice(mat):
    res = {}
    mean = calculMean(mat)
    integ = calculIntegral(mat, mean)
    gaus = calculGaus()
    res['matrix'] = mat
    res['integral'] = integ
    res['mean'] = mean
    return res

def calculMean(mat):
    mean = 0
    it = 0
    for i in range(len(mat[:,0])):
        #cond = (float(mat[i,0]) > float(-3*np.exp(-8)))
        #cond = (float(mat[i, 0]) > float(-1*np.exp(-8)))
        if (float(mat[i,0]) > float("-3.0e-08")) & (float(mat[i, 0]) < float("-1.0e-08")):
            mean += mat[i, 1]
            it += 1
    return mean / it

def calculIntegral(mat, back):
    #val = 0
    #for a in mat[:,1]:
    #    val += float(a) - float(back)
    #return val
    return np.trapz(mat[:,1], dx = back)

def calculGaus():
    return []
