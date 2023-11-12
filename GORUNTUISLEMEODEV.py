import numpy as np
import cv2
I=cv2.imread("Grey.foto.jpg",cv2.IMREAD_GRAYSCALE)
Hist=np.zeros(256,dtype=int)
m, n = I.shape
for v in range(n):
    for u in range(m):
        i = I[u, v]
        Hist[i] += 1
for i in range(256):
    print(i,':',Hist[i])

