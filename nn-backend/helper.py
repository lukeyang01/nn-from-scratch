import numpy as np
import time
import random

def shift_vector(x, center_x, center_y, size_x: int, size_y: int):
    """Given matrix x, center_x (current center), center_y (current y), 
    shift the image to be centered by adding padding."""

    true_center_x = int(size_x / 2)
    true_center_y = int(size_y / 2)

    padding_x = int(center_x - true_center_x)
    padding_y = int(center_y - true_center_y)

    if padding_x > 0:
        # Shift left
        pp_x = np.full(shape = (padding_x, x.shape[1]), fill_value=0)
        x = np.vstack(tup=(x, pp_x))
        x = x[abs(padding_x):x.shape[0], :]

    elif padding_x < 0:
        # Shift right
        pp_x = np.full(shape = (abs(padding_x), x.shape[1]), fill_value=0)
        x = np.vstack(tup=(abs(pp_x), x))
        x = x[0:size_y, :]

    if padding_y > 0:
        # Shift up
        pp_y = np.full(shape = (x.shape[0], abs(padding_y)), fill_value=0)
        x = np.hstack(tup=(x, pp_y))
        x = x[:, abs(padding_y):x.shape[1]]
        
    elif padding_y < 0:
        # Shift down
        pp_y = np.full(shape = (x.shape[0], abs(padding_y)), fill_value=0)
        x = np.hstack(tup=(pp_y, x))
        x = x[:, 0:size_x]

    return x


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date():
    return str_time_prop("1/1/2005 12:00 AM", "4/30/2024 11:59 PM", '%m/%d/%Y %I:%M %p', random.random())