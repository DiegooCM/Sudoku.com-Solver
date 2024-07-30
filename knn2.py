import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import pyautogui
from PIL import Image

df = pd.read_csv("dataset.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

prediction_array = []

for n in [0, 2, 3, 5, 6, 8, 9, 11, 12, 18, 19, 20, 23, 26, 27, 29, 30, 32, 35, 36, 37, 38, 39, 44, 45, 46, 50, 52, 55, 56, 58, 62, 64, 67, 68, 77, 78, 79]:
    image_path = f'squares/square{n}.png'

    image = Image.open(image_path).convert('L')

    image_array = np.array(image).reshape(1, -1)

    prediction = knn.predict(image_array)
    
    prediction_array.append(prediction[0])

print(prediction_array)


