import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

heart_data = pd.read_csv('heart_disease_data.csv')

heart_data.head()

heart_data.tail()

heart_data.shape

# heart_data.info()

heart_data.describe()

heart_data['target'].value_counts()

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# print(X)

# print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# print(X.shape, X_train.shape, X_test.shape)

categorical_list = ["sex", "cp","fbs","restecg","exang","slope","ca","thal","target"]

# heart_data_categoric = heart_data.loc[:, categorical_list]
# for i in categorical_list:
#     plt.figure()
#     sns.countplot(x = i, data = heart_data_categoric, hue = "target")
#     plt.title(i)

numeric_list = ["age", "trestbps","chol","thalach","oldpeak","target"]

# heart_data_numeric = heart_data.loc[:, numeric_list]
# sns.pairplot(heart_data_numeric, hue = "target", diag_kind = "kde")
# plt.show()

model = LogisticRegression()

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# print('Accuracy on Training data : ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# print('Accuracy on Test data : ', test_data_accuracy)


input_data = (63,1,	3,	145,	233,	1,	0,	150,	0,	2.3,	0,	0,	1	)

input_data_as_numpy_array= np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')