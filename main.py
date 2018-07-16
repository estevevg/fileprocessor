import functions
import utils
import sys

import numpy as np

def doPath(path):
    #Checks if the folder is well formated, if not, it is formated well
    if path[len(path) -1] != '/':
        path = path+'/'

    means = []
    integrals = []
    files = utils.getFiles(path)
    for f in files:
        if '.txt' in f:
           m =  doExercice(path+f)
           integrals.append(m["integral"])
           if m['integral'] < 0.:
               functions.plotMatrix(m, f)
               print f
           means.append(m["mean"])
           #nextGraph()
        else:
            #TODO format .trc files
            print "The file "+path+f+" is not allowed in this version"
    mhist, ma, mi, bins = functions.histogram(means)
    covariance = functions.Fitting(mhist, ma, mi, bins)

    ihist, ma, mi, bins = functions.histogram(integrals)
    functions.plot(ihist, ma, mi, bins)
    #function.plot90

def doExercice(f):
    m = functions.fileTxt2Matrix(f)
    r = functions.doExercice(m)
    #p = functions.plotMatrix(m)

    return r



def nextGraph():
    inp = raw_input("do you want to continue? Type 'no' if you want to exit: ")
    if "no" in inp:
        sys.exit("I hope you enjoy this hummble program")

def printUsageMessage():
    print "Please enter one of the options:"
    print "1. Do an entire folder"
    print "     python main.py /path/to/folder/"
    print "2. Do a specific file"
    print "     python main.py file /path/to/file"

def main():

    if len(sys.argv) < 2:
        printUsageMessage()
    elif len(sys.argv) == 2:
        doPath(sys.argv[1])
    elif len(sys.argv) == 3:
        m = doExercice(sys.argv[2])
        functions.plotMatrix(m, sys.argv[2])
    else:
        printUsageMessage()


if __name__ == '__main__':
    main()
