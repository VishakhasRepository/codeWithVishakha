import math

import numpy
import numpy as np
from scipy.stats import stats

array = numpy.array([17, 27, 80, 39, 72, 95, 52, 85, 8, 64, 36, 15, 62, 76, 66, 67, 59, 92])
print(np.average(array))

IQR = stats.iqr(array, interpolation = 'midpoint')

print(IQR)