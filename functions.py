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
def plotMatrix(mat):
    plt.plot(mat[:, 0], mat[:, 1])
    plt.ylabel('Ampl')
    plt.xlabel('Time')

    plt.show()

def doExercice(mat):
    #TODO do the exercice with the matrix
    return mat
