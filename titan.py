import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing  import LabelBinarizer

df = pd.read_csv('titanic_full.csv')
df.info()

# print(df.shape)
# print(df.describe())
# print(df.Age.describe())
# print(df.Age.quantile(0.25))
# print(f'IQR: {(39-21)}')
# print(f'{39 + ((39-21) *1.5)} - {21-((39-21) * 1.5)}')



# df.Survived.value_counts().plot(kind="bar")
# # plt.show()
# df.Survived.value_counts(normalize=True).plot(kind="bar")
#
# plt.subplot2grid((2,3), (0,1))
# plt.scatter(df.Survived, df.Age)
#
# plt.subplot2grid((2,3), (0,2))
# df.Pclass.value_counts().sort_index().plot(kind="barh")
#
# plt.subplot2grid((2,3),(1, 0))
# # df.Age(df.Pclass == 1).plot(kind="kde")
# # df.Age(df.Pclass == 2).plot(kind="kde")
# # df.Age(df.Pclass == 3).plot(kind="kde")
# for _ in df.Pclass.unique():
#     df.Age[df.Pclass == _].plot(kind="kde")
# plt.legend(df.Pclass.unique())
#
# plt.subplot2grid((2,3), (1,2))
# df.Embarked.value_counts().plot(kind="bar")
#
#
# plt.subplots_adjust(hspace=0.5)
# plt.show()

import numpy as np

sex = pd.get_dummies(df['Sex'], drop_first=True)
embarked = pd.get_dummies(df['Embarked'], drop_first=True)

lbinarizer = LabelBinarizer()
pclass = lbinarizer.fit_transform(df["Pclass"])
print(pclass)
pclass = pd.DataFrame(pclass, columns=lbinarizer.classes_, dtype=np.int8)

from scipy.stats import shapiro, mannwhitneyu

print(shapiro(df.Age[df.Age.notnull()]))
print(mannwhitneyu(df[df.Pclass == 1 & df.Age.notnull()].Age, df[df.Pclass == 3 & df.Age.notnull()].Age))
# print(df.loc[df.Age.isnull(), "Age"])

df.loc[df.Age.isnull(), "Age"] = df.groupby('Pclass').Age.transform('median')
df.info()

df = pd.concat([df, sex, pclass, embarked], axis=1)

df.drop(['Sex','Embarked', 'Ticket', 'Name', 'PassengerId'], axis=1, inplace=True)

y = df.Survived.values
X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'male', 'Q', 'S']].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=100)
print(X_train, X_test, y_train, y_test)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_auc_score, roc_curve

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

logreg_auc_score = round(logreg.score(X_train, y_train) *100, 2)
#Mean Accuracy