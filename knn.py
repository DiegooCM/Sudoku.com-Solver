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

image_path = 'squares/square3.png'
image = Image.open(image_path).convert('L')  # Convertir a escala de grises
image = image.resize((28, 28), Image.ANTIALIAS)  # Redimensionar a 28x28 píxeles

# Paso 2: Convertir la imagen a un array de numpy y aplanarla
image_array = np.array(image).reshape(1, -1)

# Paso 3: Escalar la imagen usando el mismo escalador que para los datos de entrenamiento
image_scaled = scaler.transform(image_array)

plt.imshow(image, cmap='gray')
plt.title("Imagen redimensionada a 28x28")
plt.show()

# Paso 4: Hacer la predicción
predicted_label = knn.predict(image_scaled)

print(f'La imagen ha sido clasificada como: {predicted_label[0]}')