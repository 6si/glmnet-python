import numpy as np
from ..glmnet import ElasticNet
from sklearn.datasets import make_regression
from ..cv.cv_glmnet import CVGlmNet

display_bar = '-'*70

X, y = make_regression(
    n_samples = 5000,
    n_features = 100,
    n_informative = 40,
    effective_rank = 30,
    noise = 8,
)

print display_bar
print "Cross validate an elastic net on some fake data"
print display_bar

enet = ElasticNet(alpha=.1)
enet_cv = CVGlmNet(enet, n_jobs=1)
enet_cv.fit(X, y)

print display_bar
print enet_cv.base_estimator

enet_cv.plot_oof_devs()