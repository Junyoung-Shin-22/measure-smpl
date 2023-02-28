import numpy as np

def on_y(vertices, face, y):
    top = max(vertices[face,1])
    bottom = min(vertices[face,1])
    return bottom <= y <= top

def loop_length(vertex, idx):
    l = 0
    for i, current in enumerate(idx):
        previous = idx[i-1]
        l += np.linalg.norm(vertex[current,:] - vertex[previous,:])

    return l