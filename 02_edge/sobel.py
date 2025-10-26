# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk eksperimen edge detection metode sobel

from skimage.color import rgb2gray
from scipy.ndimage import sobel
import numpy as np
from util import showImages
        
def sobelThreshold(images, thresholds: list[int]):
    """
    Melakukan deteksi tepi menggunakan operator Sobel, kemudian menerapkan threshold.

    Parameter:
    - images: daftar gambar input
    - thresholds: daftar nilai ambang magnitude gradien
    """
    for image in images:
        res_images = [image]
        titles = ["original"]
        
        if image.ndim == 3:
            image = rgb2gray(image)

        for t in thresholds:
            h = sobel(image, 0)
            v = sobel(image, 1)
            magnitude = np.sqrt(h**2 + v**2)
            
            magnitude = magnitude > t
            res_images.append(magnitude)
            titles.append(f"threshold {t}")
        
        showImages(res_images, titles)