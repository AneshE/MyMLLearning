#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier
kClassifier = KNeighborsClassifier(n_neighbors=8)
#kClassifier.fit(features_train, labels_train)
#print kClassifier.score(features_test, labels_test) # 0.944

from sklearn.ensemble import RandomForestClassifier
rfClassifier = RandomForestClassifier(min_samples_split=5)
#rfClassifier.fit(features_train, labels_train)
#print rfClassifier.score(features_test, labels_test) # 0.92

from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
svc = SVC(kernel='linear', probability=True)
abClassifier = AdaBoostClassifier(n_estimators=15, learning_rate=1)
abClassifier.fit(features_train, labels_train)
print abClassifier.score(features_test, labels_test) #0.928






try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
