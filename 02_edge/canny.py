# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk eksperimen edge detection metode canny

from skimage.color import rgb2gray
from skimage import feature
from util import showImages
        
def cannySigma(images, sigma: list[int]):
    """
    Menerapkan deteksi tepi menggunakan metode Canny dengan berbagai nilai sigma.

    Parameter:
    - images: daftar gambar input
    - sigma: daftar nilai sigma 
    """
    for image in images:
        res_images = [image]
        titles = ["original"]

        if image.ndim == 3:
            image = rgb2gray(image)

        for s in sigma:
            res = feature.canny(image, sigma=s)
            res_images.append(res)
            titles.append(f"sigma {s}")
        
        showImages(res_images, titles)