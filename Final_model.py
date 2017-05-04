#Building the classifier on final merged dataset
import pandas as pd
import datetime
from sklearn import tree
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
file = pd.read_csv('Merge1.csv')

#removing duplicates from the dataset
file.drop_duplicates(subset = ['ApplNoSimple'], inplace = True)
file['year'] = file['Appl_Year']
file.shape #(763968, 752)

#splitting the dataset into train and test
train = file[file['year'] <= 2010]
train.shape #(626309, 752)
test = file[file['year'] > 2010]
test.shape #(137659, 752)

#selecting the required features in the dataset for training classifier
train = train.ix[:, [32,33,37,40,43,46,48,49,50,51,55,56,57,731,732,733,750]+list(range(60,730))]
train.shape #(626309, 687)
test = test.ix[:, [32,33,37,40,43,46,48,49,50,51,55,56,57,731,732,733,750]+list(range(60,730))]

#removing missing rows or observations, if any of them are present
train.dropna(axis = 0, how = 'any', inplace = True)
train.shape #(626110, 687)
test.dropna(axis = 0, how = 'any', inplace = True)
test.shape # (137577, 687)

#predictors
x_train2 = train.ix[:,1:]
x_test2 = test.ix[:,1:]

#response variable
y_train = train['Granted_x']
y_test = test['Granted_x']

#building Decision tree classifier
clf2 = tree.DecisionTreeClassifier()
#fitting the classifier
clf2 = clf2.fit(x_train2, y_train)
#predicting the response on test dataset
y_pred2 = clf2.predict(x_test2)
print(confusion_matrix(y_test, y_pred2))

features =['Inventor_Count','AR_ICountry','AR_ICity','AR_ACountry','AR_ACity','Org_Ind','Month','SubClass_C','MainClass_C','dependent_claims','nostop_length_firstclaim','total_claims','art_unit_GRate','examiner_GRate','Year_Similarity','cosine']+['mainclass']*670
len(features) #686
len(clf2.feature_importances_)
#feature importance given by decision tree classifier
print(sorted(list(zip(clf2.feature_importances_, features))))
#nostop_length_firstclaim(0.23017), examiner_Grate (0.1436),art_unit_grate(0.129079),AR_I_city(0.06105), Acity(0.053809), cosine(0.04337732),year_similarity(0.024598),total_claims(0.024354), dependent claims(0.0193288),month(0.0181509), subclass_C(0.01530055), inventor count(0.0137569), icountry(0.009).acountry(0.010144),mainclass matrix

#building logistic regression classifier
logreg2 = linear_model.LogisticRegression()
#fitting the classifier
logreg2 = logreg2.fit(x_train2,y_train)
#predicting the response on test dataset
y_pred4 = logreg.predict(x_test2)
print(confusion_matrix(y_test, y_pred4))


########################################
#Data visualization
#splitting the dataset into granted and not granted
granted = file[file['Granted_x'] == 1]
ungranted = file[file['Granted_x'] == 0]

#average total number of claims
granted['total_claims'].mean()
ungranted['total_claims'].mean()

#average number of dependent claims
granted['dependent_claims'].mean()
ungranted['dependent_claims'].mean()

#average length of first independent claim
granted['nostop_length_firstclaim'].mean()
ungranted['nostop_length_firstclaim'].mean()

#description statistics of dependent claims, total numbe rof claims and length
of first independent claim
granted['dependent_claims'].describe()
ungranted['dependent_claims'].describe()
granted['total_claims'].describe()
ungranted['total_claims'].describe()
granted['nostop_length_firstclaim'].describe()
ungranted['nostop_length_firstclaim'].describe()

#boxplot of total number of claims for granted and not granted patents
sub = file[['total_claims','Granted']]
sub.boxplot('total_claims', by = 'Granted')
plt.ylim(0,60)
plt.show()

##boxplot of number of dependent claims for granted and not granted patents
sub = file[['dependent_claims','Granted']]
sub.boxplot('dependent_claims', by = 'Granted')
plt.ylim(0,50)
plt.show()

##boxplot of length of first independent claim for granted and not granted patents
sub = file[['length_of_first_independent_claim','Granted']]
sub.boxplot('length_of_first_independent_claim', by = 'Granted')
plt.ylim(0,300)
plt.show()

#boxplot of cosine similarity for granted and not granted patents
sub = file[['cosine','Granted']]
sub.boxplot('cosine', by = 'Granted')
plt.ylim(0,1.1)
plt.show()





