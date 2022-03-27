import arraytool.planar as planar
import numpy as np

a = 0.6 # separation between the elements along x-axis (normalized WRS wavelength)
b = 0.5 # separation between the elements along y-axis (normalized WRS wavelength)
M = 10 # no. of elements along x-axis
N = 11 # no. of elements along y-axis

A = np.ones((N, M)) # Uniform planar excitation

# Converting the 'excitation & position' information into Arraytool input format
array_ip = planar.ip_format(a, b, A)


# Calling the 'pattern_uv' function to evaluate and plot 3D AF/GF/NF
[u, v, AF] = planar.pattern_uv(array_ip, u_scan=0, v_scan=0, u_min= -2, u_max=2, u_num=300,
           v_min= -2, v_max=2, v_num=300, scale="dB", dB_limit=-40,
           factor="NF", plot_type="contour", mayavi_app=False)


# Calling the 'pattern_uv' function to evaluate and plot 3D AF/GF/NF
#[u, v, AF] = planar.pattern_uv(array_ip, u_scan=0, v_scan=0, u_min= -2, u_max=2, u_num=300,
#           v_min= -2, v_max=2, v_num=300, scale="dB", dB_limit=-40,
#           factor="NF", plot_type="rect", mayavi_app=False)
