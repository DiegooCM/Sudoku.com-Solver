import tensorflow as tf


mnist = tf.keras.datasets.mnists

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(26, 26)))
model.add(tf.keras.layers.Dense(128, activation='relu'))# Se puede poner lo que sea en el str, Relu = rectify linear unit
model.add(tf.keras.layers.Dense(128, activation= 'relu'))
model.add(tf.keras.layers.Dense(9, activation='softmax')) #9 por los 9 números, esto es el 'output'. Investigar acerca del activation

model.compile(optimizer= 'adam', loss= 'sparse_categorical_crossentropy', metrics = ['accuracy'])#Lo compilamos

model.fit(x_train, y_train, epochs= 3) # Lo entrenamos

model.save('model1.model')