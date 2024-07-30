import pickle
import cv2
from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from PIL import Image

'''
ME PREDICE TODOS LOS NÚMEROS COMO 2
'''


# Carga el dataset MNIST
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"], mnist["target"]

# Convertir las etiquetas a enteros
y = y.astype(np.int64)

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear y entrenar el modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Realizar predicciones
y_pred = knn.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo KNN: {accuracy * 100:.2f}%')


'''with open('knn_model.pickle','wb') as f:
	pickle.dump(knn, f)

pickle_in = open('knn_model.pickle','rb')


clf = pickle.load(pickle_in)
'''
# Aquí estamos creando una imagen aleatoria para el ejemplo

predictions_array = []

for n in [0, 2, 3, 5, 6, 8, 9, 11, 12, 18, 19, 20, 23, 26, 27, 29, 30, 32, 35, 36, 37, 38, 39, 44, 45, 46, 50, 52, 55, 56, 58, 62, 64, 67, 68, 77, 78, 79]:
    
	image_path = f'squares/square{n}.png'
	image = Image.open(image_path).convert('L') 
	image = image.resize((28, 28), resample=Image.BILINEAR)

	image_array = np.array(image).reshape(1, -1)

	image_scaled = scaler.transform(image_array)

	predicted_label = knn.predict(image_array)

	predictions_array.append(predicted_label[0])

print(predictions_array)