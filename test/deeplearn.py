import tensorflow as tf
import numpy as np 

path=r'D:\\BaiduNetdiskDownload\\hello\\.vscode\\deeplearn\\DeepLearn\\test\\mnist.npz'
f = np.load(path)
x_train, y_train = f['x_train'], f['y_train']
x_test, y_test = f['x_test'], f['y_test']
x_train, x_test = x_train / 255.0, x_test / 255.0

print(x_train.shape  ,  y_train.shape )
print ( x_train)
print ( y_train ) 

'''
Generally, all layers in Keras need to know the shape of their inputs
in order to be able to create their weights.
'''
model = tf.keras.models.Sequential([
  # tf.keras.layers.Input(shape=() ),
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train,  batch_size= 25 , epochs=5)

model.summary() 
model.evaluate(x_test,  y_test, verbose=2)
# print(x_test.shape)
# print(y_test)
# model.save('mymodel')
