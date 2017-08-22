from __future__ import division
import numpy as np
from numpy.random import randint

samples = 1000
max_bdays = 100
duplicates = []

for bd in xrange(1, max_bdays):
    duplicates.append(sum([len(set(randint(1,365,bd))) < bd
                           for i in xrange(0, samples)]))

print np.array(duplicates) / samples
