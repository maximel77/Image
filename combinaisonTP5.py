import matplotlib.pyplot as plt
import numpy as  np
from PIL import Image

image1=Image.open("doc1.jpg")
image2=Image.open("doc4.jpg")


image1_array=np.array(image1)
image2_array=np.array(image2)


combined_image = np.concatenate((image2_array, image1_array), axis=1)

# Convertir le tableau numpy combiné en image PIL
combined_image = Image.fromarray(combined_image)

# Afficher l'image combinée
plt.imshow(combined_image)
plt.axis('off')  # Masquer les axes
plt.savefig("combinaison2")
plt.show()

# Sauvegarder l'image combinée
combined_image.save('combined_image1.jpg')

