import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
from joblib import dump, load
import numpy

def acc(y_test,test_predict):
    Accuracy = accuracy_score(y_test, test_predict)
    print("Accuracy :")
    print(Accuracy)

    precision=precision_score(y_test, test_predict, average='micro')
    print("precision :")
    print(precision)

    recall=recall_score(y_test, test_predict, average='micro')
    print("recall :")
    print(recall)

    f1_micro=f1_score(y_test, test_predict, average='micro')
    print("f1_micro :")
    print(f1_micro)

    f1_macro=f1_score(y_test, test_predict, average='macro')
    print("f1_macro :")
    print(f1_macro)

def train(X_train, X_test, y_train, y_test):
    clf_multilabel = OneVsRestClassifier(RandomForestClassifier())

    model = clf_multilabel.fit(X_train, y_train)

    pred = model.predict(X_test)
    print(pred)
    # 模型评估
    # error_rate=np.sum(pred!=test.lable)/test.lable.shape[0]
    error_rate = np.sum(pred != y_test) / y_test.shape[0]
    print('测试集错误率(softmax):{}'.format(error_rate))

    accuray = 1 - error_rate
    print('测试集准确率：%.4f' % accuray)
    # 模型保存
    joblib.dump(model, 'rf.joblib')

#读入数据
dataset = pd.read_csv('../../csv/origin/TrainSET.csv', engine='python')

# split dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(dataset.iloc[:, :-1], dataset.iloc[:, -1], test_size=0.2, random_state=123)

#模型训练
train(X_train, X_test, y_train, y_test)

# 模型预测
data = numpy.loadtxt(open("../../csv/origin/PredictSET.csv","rb"),delimiter=",",skiprows=0)

label=numpy.loadtxt(open("../../csv/origin/PredictSETLabel.csv","rb"),delimiter=",",skiprows=0)

x_pred = np.array(data)
y_true=np.array(label)

#加载模型
clf = joblib.load('rf.joblib')
y_pred = [round(value) for value in clf.predict(x_pred)]
print('y_pred：', y_pred)
acc(y_true, y_pred)

# Accuracy :
# 0.961376404494382
# precision :
# 0.961376404494382
# recall :
# 0.961376404494382
# f1_micro :
# 0.961376404494382
# f1_macro :
# 0.7536273740716687