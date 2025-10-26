# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk eksperimen filter gaussian

from scipy.ndimage import gaussian_filter
from util import showImages

def gaussianStrength(images, sigma: list[int], mode='reflect'):
    """
    Menerapkan gaussian filter pada gambar dengan berbagai nilai sigma untuk menunjukkan pengaruh tingkat blur.

    Parameter:
    - images: daftar gambar yang akan diproses
    - sigma: daftar nilai sigma
    - mode: metode penanganan tepi (default 'reflect')
    """
    for image in images:
        res_images = [image]
        titles = ["original"]
        for s in sigma:
            res = gaussian_filter(image, sigma=s, mode=mode)
            res_images.append(res)
            titles.append(f"sigma {s}")
        
        showImages(res_images, titles)
        
def gaussianMode(images, modes: list[str], sigma=10):
    """
    Menerapkan gaussian filter pada gambar dengan berbagai mode untuk menunjukkan pengaruh penanganan tepi.

    Parameter:
    - images: daftar gambar input
    - modes: daftar mode (misal: 'reflect', 'nearest', 'constant', dst.)
    - sigma: nilai sigma tetap untuk semua percobaan (default = 10)
    """
    for image in images:
        res_images = [image]
        titles = ["original"]
        for m in modes:
            res = gaussian_filter(image, sigma=sigma, mode=m)
            res_images.append(res)
            titles.append(f"mode {m}")
        
        showImages(res_images, titles)