import matplotlib.pyplot as plt
import numpy as  np
from PIL import Image

image=Image.open("doc4.jpg").convert('L')
image_array=np.array(image)
projection_v=np.sum(image_array,axis=1)
taille= len(projection_v)
i=0
compteur=0
m=max(projection_v)
# Calculer un seuil basé sur le percentile des valeurs de projection
percentile_val = np.percentile(projection_v, 10)  # Par exemple, le 10e percentile
val = percentile_val


while i< taille:
    if projection_v[i]<val:
        compteur+=1
        i+=10
    i+=1
print(compteur)
plt.figure(figsize=(10, 6))
plt.plot(projection_v)
plt.title("Histogramme de Projection Verticale")
plt.xlabel("Ligne")
plt.ylabel("Somme des pixels")

plt.show()
