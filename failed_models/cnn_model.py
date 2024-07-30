import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1), activation='relu'))
        # Add a Max pooling layer
model.add(tf.keras.layers.MaxPool2D())
        # Add the flattened layer
model.add(tf.keras.layers.Flatten())
        # Add the hidden layer
model.add(tf.keras.layers.Dense(512, activation='relu'))
        # Adding a dropout layer
model.add(tf.keras.layers.Dropout(0.2))
        # Add the output layer
model.add(tf.keras.layers.Dense(10, activation='softmax'))
        # Compiling the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs= 5) # Lo entrenamos

model.save('cnn_model.keras') 