
import numpy as np
from PIL import Image
def see_gaussian(seuil):
    image= Image.open("gaussian.png")
    n= np.asarray(image)
    
    rouge_8= n[:,:,0].astype(np.uint8)
 
    im=np.zeros(image.size)
    compteur=0
    for i in range(image.size[0]):
        for j in range(image.size[0]):
           if rouge_8[i][j]>seuil:
               im[i][j]=1
               compteur+=1
    
    return im,compteur,compteur/(image.size[0]*image.size[1])


    
