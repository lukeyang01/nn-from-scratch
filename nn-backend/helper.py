import numpy as np

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
        print(x.shape)
        x = x[abs(padding_x):x.shape[0], :]


    elif padding_x < 0:
        # Shift right
        pp_x = np.full(shape = (abs(padding_x), x.shape[1]), fill_value=0)
        x = np.vstack(tup=(abs(pp_x), x))
        print(x.shape)
        x = x[0:size_y, :]
        print(x.shape)

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