#######################################
# Zane Rossi
# University of Chicago
# PGS Lab: June, 2016
#######################################

from numpy import *
from collections import *
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import os
from scipy.interpolate import interp1d

#######################################
# Instantiation of grid structure and duration
# as wel as various other electromagnetic constants
#######################################

# arbitrary dimension determined by other constants
FIELD_SIZE = 100
# arbitrary dimension determined by other constants
DURATION = 2000
# wavelength of light to be investigated in nm
# will be changed to list
WAVELENGTH = 1000
# outside specification of layer sturcture
# start position, end position, index of refraction (possible lookup), and
# whether the layer E^2 is to be actively calculated
layer = namedtuple('layer',['start','stop','index','active'])
# barrier is a list of layers
BARRIER = []


def main():
	print("There is nothing here yet.")


if __name__ == "__main__":
	main()