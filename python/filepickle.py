" Utility for save and reload objects without flat files"
import pickle

def saveDbase(filename, object):
    filr = open(filename, 'wb')
    pickle.dump(object, file)
    filr.close()

def loadDbase(filename):
    file = open(filename, 'rb')
    object = pickle.load(file)
    file.close()
    return object
