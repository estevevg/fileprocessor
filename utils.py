from os import listdir
from os.path import isfile, join

# Gets all the files in a specified path (ex: /home/maria/dades)
def getFiles(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles
