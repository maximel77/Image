import numpy as np
from PIL import Image
def see_gaussian(seuil):
    image= Image.open("gaussian.png")
    n= np.asarray(image)
    
    rouge_8= n[:,:,0].astype(np.uint8)
 
    im=np.zeros(image.size)
    compteur=0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
           if rouge_8[i][j]>seuil:
               im[i][j]=1
               compteur+=1
    
    return im,compteur,compteur/(image.size[0]*image.size[1])

def see_gaussian_rouge(seuil):
    image= Image.open("shapes.png")
    n= np.asarray(image)
    
    rouge_8= n[:,:,0].astype(np.uint8)
 
    im=np.zeros(image.size)
    compteur=0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
           if rouge_8[i][j]>seuil:
               im[i][j]=1
               compteur+=1
    
    return im*255

def  see_gaussian_vert(seuil):
    image= Image.open("shapes.png")
    n= np.asarray(image)
    
    vert_8= n[:,:,1].astype(np.uint8)
 
    im=np.zeros(image.size)
    compteur=0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
           if vert_8[i][j]>seuil:
               im[i][j]=1
               compteur+=1
    
    return im*255

def  see_gaussian_bleu(seuil):
    image= Image.open("shapes.png")
    n= np.asarray(image)
    
    bleu_8= n[:,:,2].astype(np.uint8)
 
    im=np.zeros(image.size)
    compteur=0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
           if bleu_8[i][j]>seuil:
               im[i][j]=1
               compteur+=1
    
    return im*255


def see_shapes(obj):
    image=Image.open("shapes.png")
    n=np.asarray(image)
    im=np.zeros(image.size)
    vert_8=n[:,:,1]
    bleu_8=n[:,:,2]
    match obj:
        case "oval":
            return see_gaussian_rouge(160)
        case "star":
            return see_gaussian_vert(150)
        case "rectangle":
            return see_gaussian_bleu(150)
        case "heart":
            im1=see_gaussian_rouge(130)
            im2=see_gaussian_vert(128)
            
            for i in range(image.size[0]):
                for j in range(image.size[1]):
                    if im1[i][j]==im2[i][j]==255:
                        im[i][j]=255
            return im
        case "chat":
            return see_gaussian_vert(10)

    
            
            
    


r=see_gaussian

print(see_gaussian(30))
print(see_shapes("heart"))
image=Image.fromarray(see_shapes("heart"))
image.show()
