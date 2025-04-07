from PIL import Image
import numpy as np


image_path = "shapes.jpg"
image = Image.open(image_path)
image_gray = image.convert("L")
image_gray.save("image_gris.jpg")

def proconv(image, filtre):
    
    h, l = image.size
    
   
    ker = len(filtre)
    moy = ker // 2  
    
    
    m_image = np.array(image)
    
    
    conv = np.zeros_like(m_image)
    
    
    for i in range(l):
        for j in range(h):
            somme = 0
            for i1 in range(-moy,moy+1):
                for j1 in range(-moy,moy+1):
                   
                    if 0 <= i + i1  < l and 0 <= j + j1  < h:
                        valeurpixel=m_image[i+i1][j+j1]
                    else:
                        valeurpixel=0
                    valeurpixelfiltre=m_image[-i1+moy][-j1+moy]
                    somme+=valeurpixelfiltre*valeurpixel
            conv[i,j]=somme
                    
            
            
             

  
    return Image.fromarray(conv.astype(np.uint8))


f1 = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]


image_conv = proconv(image_gray, f1)


image_conv.show()
