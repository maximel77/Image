import matplotlib.pyplot as plt
import numpy as  np
from PIL import Image
from PIL import ImageOps
image=Image.open("doc4.jpg").convert('L')




# Appliquer un seuillage adaptatif ou global pour binariser l'image
threshold = 128  # Par exemple, seuil à 128 (modifiable selon l'image)
image_bin = image.point(lambda p: p > threshold and 255)  # Binarisation de l'image
image_array_bin = np.array(image_bin)

# Recalculer la projection verticale sur l'image binarisée
projection_v = np.sum(image_array_bin, axis=1)

plt.figure(figsize=(10, 6))
plt.plot(projection_v)
plt.title("Histogramme de Projection Verticale")
plt.xlabel("Ligne")
plt.ylabel("Somme des pixels")

plt.show()
