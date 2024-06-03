# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    return np.sum(np.square(np.reshape(new_points, (len(new_points), 1,-1)) - points), axis=2)
