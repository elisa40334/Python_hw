import matplotlib.pyplot as plt
import numpy as np

sample_id = []
for i in range(10):
    p = np.argwhere(y_train==i).ravel()[:10]
    sample_id.extend(p)
sel_img = x_train[sample_id]  
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(sel_img.reshape((10,10,28,28)).transpose((1,2,0,3)).reshape((-1,280)),cmap='gray')
plt.axis(False)
plt.title('reshape((10,10,28,28)).transpose((1,2,0,3))')
plt.subplot(1,3,2)
plt.imshow(sel_img.reshape((10,10,28,28)).transpose((0,2,1,3)).reshape((-1,280)),cmap='gray')
plt.axis(False)
plt.title('reshape((10,10,28,28)).transpose((0,2,1,3)')
plt.subplot(1,3,3)
plt.imshow(sel_img.reshape((5,2,10,28,28)).transpose((1,0,3,2,4)).reshape((-1,280)),cmap='gray')
plt.axis(False)
plt.title('reshape((5,2,10,28,28)).transpose((1,0,3,2,4))')
plt.show()