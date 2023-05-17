import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

#创建数据
x=np.linspace(0,1,100).reshape(-1,1)

y=[i*np.random.uniform(0.5,0.7) for i in np.linspace(0,1,100)]
y=np.array(y)

model=LinearRegression()
model.fit(x,y)
y_pred=model.predict(x)


with open('model/model.pkl', 'wb') as file:
    print("储存文件！")
    pickle.dump(model, file)

