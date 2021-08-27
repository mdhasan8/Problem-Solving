# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 11:23:08 2021

@author: Easin
"""
'''
import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
#alphas = np.logspace(-6, 6, 13)
#print(alphas)
fit = reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
alpha_coef = reg.alpha_
print(fit)
print(alpha_coef)

'''
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# X is the 10x10 Hilbert matrix
X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
print(X)
y = np.ones(10)
print(y)
print( np.arange(0, 10))#[:, np.newaxis])
# #############################################################################
# Compute paths

n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)
print(alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
print(coefs)
print(len(coefs[0]))

# #############################################################################
# Display results

ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])  # reverse axis
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()