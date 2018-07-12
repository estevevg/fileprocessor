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
    mean = calculMean(mat[:,1], 10)
    integ = calculIntegral(mat[:,1], mean)
    gaus = calculGaus()
    res['matrix'] = mat
    res['integral'] = integ
    res['mean'] = mean
    return res

def calculMean(arr, lim):
    if lim > len(arr):
        lim = len(arr)
    summ = 0
    for i in range(lim):
        summ += arr[i]
    return summ / lim

def calculIntegral(arr, back):
    val = 0
    for a in arr:
        val += a - back
    return val

def calculGaus():
    return []
