# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk eksperimen filter median

from scipy.ndimage import median_filter
from util import showImages

def medianSize(images, size: list[int], mode='reflect'):
    """
    Menerapkan median filter pada gambar dengan berbagai ukuran kernel.

    Parameter:
    - images: daftar gambar input
    - size: daftar ukuran kernel filter median
    - mode: metode penanganan tepi (default 'reflect')
    """
    for image in images:
        res_images = [image]
        titles = ["original"]
        for s in size:
            res = median_filter(image, size=s, mode=mode)
            res_images.append(res)
            titles.append(f"size {s}")
        
        showImages(res_images, titles)
        
def medianMode(images, modes: list[str], size=20):
    """
    Menerapkan median filter pada gambar dengan berbagai mode untuk menunjukkan pengaruh penanganan tepi.

    Parameter:
    - images: daftar gambar input
    - modes: daftar mode penanganan tepi (misal: 'reflect', 'nearest', 'constant')
    - size: ukuran kernel median (default = 20)
    """
    for image in images:
        res_images = [image]
        titles = ["original"]
        for m in modes:
            res = median_filter(image, size=size, mode=m)
            res_images.append(res)
            titles.append(f"mode {m}")
        
        showImages(res_images, titles)