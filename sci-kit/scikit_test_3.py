#import dataset
from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.5)

from sklearn import tree
clf_1 = tree.DecisionTreeClassifier()
clf_1 = clf_1.fit(x_train , y_train)

predictions_1 = clf_1.predict(x_test)
print(predictions_1,"\n")

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions_1),"\n")

from sklearn.neighbors import KNeighborsClassifier
clf_2 = KNeighborsClassifier()
clf_2 = clf_2.fit(x_train , y_train)

predictions_2 = clf_2.predict(x_test)
print(predictions_2,"\n")

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions_2),"\n")