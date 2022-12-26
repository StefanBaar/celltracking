import numpy as np

def circles():
    def circ(X):
        return (np.sin(X/200.*np.pi)*175).astype(int) 
    
    frames = np.zeros((20,200,200),dtype="int")

    path_x = np.arange(0,200).astype(int)

    for n,i in enumerate(frames):
        frames[n] = circ(path_x)
    
    return frames
    
