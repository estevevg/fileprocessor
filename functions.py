import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


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
    #gaus = calculGaus()
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
    val = 0
    for a in mat[:,1]:
        val += float(a) - float(back)
        #print val
    #print 'integral: ' + str(val)
    #print 'nest'
    #if val < 0.:
     #   plotMatrix(mat, f)
    return val
    #return np.trapz(mat[:,1], dx = back)

def histogram(means):
    ma, mi = np.amax(means), np.amin(means)
    print ma, mi
    bins =50

    dif = (ma-mi)/bins
    ints = np.zeros(bins)
    for i in xrange(bins):
        for j in means:
            if j >= mi + i*dif and j <= mi + (i+1)*dif:
                ints[i] += 1

    #print ints #just to show the distribution of the bins
    #plots the histogram
    plt.hist(means, bins, alpha= 0.3)
    fig = plt.gcf()
     
    return ints, ma, mi, bins

def Fitting(y, ma, mi, bins):
    
    xx = np.linspace(mi, ma, bins)
 
    popt, pcov = curve_fit (gauss, xx, y, p0 = [80,  -0.0001, 0.0002])
    

    plt.plot(xx, y, 'go')
    plt.plot(xx, gauss(xx, *popt), 'r-')
    plt.title('Baselines distribution')
    plt.ylabel('Frequency')
    plt.xlabel('value')

    plt.show()

    print 'Optimized parametres: height: ' + str(popt[0]) 
    print 'Central position: ' + str(popt[1])  
    print 'Width / variance: ' + str(popt[2])

    return popt[2]

def gauss(x, a, b, c): 
    # a: height      b: centre       c: width   
    return  a * np.exp(-1*(x-b)**2/(2 * c**2)) 

def plot(y, ma, mi, bins):
    #print y
    xx = np.linspace(mi, ma, bins)
    print y, xx
    plt.plot(xx, y, 'ro')
    plt.title('Integral distribution')
    plt.ylabel('frequency ')
    plt.xlabel('integral')
    plt.show()
