# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk eksperimen deteksi fitur dengan FAST

import cv2
from util import showImages
        
def fast(images):
    """
    Menerapkan algoritma FAST untuk mendeteksi keypoint features pada gambar.

    Parameter:
    - images: daftar gambar input
    """
    for image in images:
        res_images = [image]
        titles = ["original"]

        fast = cv2.FastFeatureDetector_create()
        kp = fast.detect(image,None)
        res = cv2.drawKeypoints(image, kp, None)

        res_images.append(res)
        titles.append(f"key points")
        
        showImages(res_images, titles)