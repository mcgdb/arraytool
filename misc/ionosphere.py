from cmath import sin, cos


def elevation_error(dr, el, Rs, R0, h):
    """Calculates the elevation error, d-el from the following parameters:
    
    :param dr:
    :param el: 
    :param Rs: Range to the target from sensor
    :param R0: Distance from the center of the earth to the sensor
    :param h: height of the ionosphere centroid
    :returns: delta el, i.e. the elevation error

    """
    top = dr * cos(el * (sin(el + (Rs / R0))))
    bottom = Rs * (((R0 + h) ** 2 / R0 ** 2) - cos(el) ** 2)
    return top / bottom


if __name__ == '__main__':
    pass
