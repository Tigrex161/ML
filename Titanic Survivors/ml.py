import csv
import numpy as np
import pandas as pd
import matplotlib
import math
import seaborn as sb
from matplotlib import pyplot as plt

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv('train.csv', sep =',')
df2 = pd.read_csv('test.csv', sep =',')
df3 = pd.read_csv('gender_submission.csv', sep= ',')


pclass = []
embark = []
labels_train = []
features_test = []
labels_test = []

df['Age'].fillna(df['Age'].median(), inplace=True)


survived_sex = df[df['Survived']==1]['Sex'].value_counts()
dead_sex = df[df['Survived']==0]['Sex'].value_counts()

d = pd.DataFrame([survived_sex, dead_sex])

d.index = ['Survived', 'Dead']


d.plot(kind='bar',stacked=True, figsize=(20,12))

plt.show()


figure = plt.figure(figsize=(20,12))


plt.hist([df[df['Survived']==1]['Fare'],df[df['Survived']==0]['Fare']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Survived','Dead'])
plt.xlabel('Fare')
plt.ylabel('Number of passengers')
plt.legend()
plt.show()






#for r in range(0,len(df2.index)):
#	features_test.append([df2.values[r][1],df2.values[r][10]])
		



#for r1 in range(0,len(df3.index)):
#	labels_test.append(df3.values[r1][1])



#for row in range(0,len(df.index)):
#	pclass.append(df.values[row][2])		
#	embark.append(df.values[row][11])	
#	labels_train.append(df.values[row][1])	

		
#features_train = []
#for x in range(0,len(df.index)):
#	features_train.append([pclass[x], embark[x]])


#for x in range(len(features_train)):
#	if features_train[x][1] == 'S': 
#		features_train[x][1] = 0
	
#	if features_train[x][1] == 'Q': 
#		features_train[x][1] = 1
	
#	if features_train[x][1] == 'C': 
#		features_train[x][1] = 2


#for x in range(len(features_test)):
#	if features_test[x][1] == 'S': 
#		features_test[x][1] = 0
	
#	if features_test[x][1] == 'Q': 
#		features_test[x][1] = 1
	
#	if features_test[x][1] == 'C': 
#		features_test[x][1] = 2



#clf = SVC(kernel = 'rbf', C = 10000, gamma = 1)

#clf = DecisionTreeClassifier(min_samples_split = 2)

#clf.fit(features_train, labels_train)
#pred = clf.predict(features_test)


#print(accuracy_score(pred,labels_test)*100)
