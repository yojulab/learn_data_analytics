import numpy as np
height, width = 150, 200
arr_img = np.zeros((height, width), np.uint8)
_img_100 = arr_img.copy()
_img_100[:, :] = 100   # gray
_img_200 = arr_img.copy()
_img_200[:, :] = 180   # gray
_img_255 = arr_img.copy()
_img_255[:, :] = 255   # gray

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 4)
axes[0].set_title("arr_img")
axes[0].imshow(arr_img, cmap='gray', vmin=0, vmax=255)
axes[1].set_title("_img_100")
axes[1].imshow(_img_100, cmap='gray', vmin=0, vmax=255)
axes[2].set_title("_img_200")
axes[2].imshow(_img_200, cmap='gray', vmin=0, vmax=255)
axes[3].set_title("_img_255")
axes[3].imshow(_img_255, cmap='gray', vmin=0, vmax=255)

plt.show()