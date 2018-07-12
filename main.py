import functions
import utils
import sys

def doPath(path):
    #Checks if the folder is well formated, if not, it is formated well
    if path[len(path) -1] != '/':
        path = path+'/'

    files = utils.getFiles(path)
    for f in files:
        if '.txt' in f:
            doExercice(path+f)
            nextGraph()
    else:
        #TODO format .trc files
        print "The file "+path+f+" is not allowed in this version"

def doExercice(f):
    m = functions.fileTxt2Matrix(f)
    r = functions.doExercice(m)
    functions.plotMatrix(r, f)

def nextGraph():
    inp = raw_input("Your highness, do you want to continue? Type 'no' if you want to exit: ")
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
        doExercice(sys.argv[2])
    else:
        printUsageMessage()


if __name__ == '__main__':
    main()
