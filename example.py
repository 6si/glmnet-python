import numpy as np
from glmnet import ElasticNet, LogisticNet

display_bar = '-'*70

print display_bar
print "Fit an elastic net on some fake data"
print display_bar

X = np.random.randn(5000, 40)
w = np.random.randn(40)
w[20:] = 0
y = np.dot(X, w)

enet = ElasticNet(alpha=1)
enet.fit(X, y)

print enet

print display_bar
print "Predictions vs. actuals for the last elastic net model:"
print display_bar

preds = enet.predict(X)
print y[:10]
print preds[:10,np.shape(preds)[1]-1]

print
print enet.deviance(X, y)
# enet.plot_path()

print
print display_bar
print "Fit a logistic net on some fake data."
print display_bar

X = np.random.randn(1000, 40)
w = np.random.randn(40)
w[20:] = 0
p = 1 /( 1 + np.exp(-np.dot(X, w)) )
y = np.float64(p > .5)

lnet = LogisticNet(alpha=.75)
lnet.fit(X, y)

print lnet 

print display_bar
print "Predictions vs. actuals for the last logistic net model:"
print display_bar

preds = lnet.predict(X)
print p[:10]
print preds[:10,np.shape(preds)[1]-1]

print 
print lnet.deviance(X, y)
#
#lnet.plot_path()