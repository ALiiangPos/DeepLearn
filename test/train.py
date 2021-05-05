import tensorflow as tf 
import numpy as np 
from tensorflow import keras 


'''
读取数据
'''
def read_data(filename) :
    label = []
    res = []
    with open(filename) as f:
        for data in f.readlines() :
            data = data.split()
            text_label = data[9:-1]
            text_res = np.array( int(data[-1]) ) 
            text_label = np.array( [ float(i) for i in text_label ] )
            label.append(text_label)
            res.append(text_res)
        return label ,res  
text , res =read_data('data.csv')
text = np.array(text)
text = text.reshape ( 2094 ,22, 16)
res = np.array(res)

''' 
建立模型
'''
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(22, 16)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax'), 
])

'''
确定模型优化器 ， 损失函数 ，指标
'''
model.compile(optimizer='Adam',
              loss='categorical_hinge',
              metrics=['accuracy'])
model.fit(text , res ,epochs=6 )
model.summary() 
# mdoel.save('test_model')