# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk display gambar

import matplotlib.pyplot as plt

def showImages(images, titles):
    n = len(images)
    _, axs = plt.subplots(1, n, figsize=(8, 8))
    plt.gray()

    for i in range(n):
        axs[i].imshow(images[i])
    
    for j, ax in enumerate(axs.ravel()):
        ax.set_title(titles[j], fontsize=8)
        ax.axis("off")
    
    plt.show()