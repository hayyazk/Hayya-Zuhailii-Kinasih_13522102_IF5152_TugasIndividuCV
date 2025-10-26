# Nama: Hayya Zuhailii Kinasih
# NIM: 13522102
# Fitur unik: Fungsi untuk eksperimen transformasi

import cv2
from util import showImages
        
def transformasi(images, src_pts, dst_pts):
    """
    Melakukan transformasi perspektif dari titik sumber ke titik tujuan, kemudian menampilkan hasil warp dan overlay antara posisi asli & hasil proyeksi.

    Parameter:
    - images: daftar gambar input
    - src_pts: koordinat sumber
    - dst_pts: koordinat tujuan
    """
    for image in images:
        res_images = [image]
        titles = ["original"]

        h, w = image.shape[:2]
        H, _ = cv2.findHomography(src_pts, dst_pts, method=0)
        warped = cv2.warpPerspective(image, H, (w, h))
        print(H)
        
        proj = cv2.perspectiveTransform(src_pts.reshape(-1,1,2), H).reshape(-1,2)

        overlay = warped.copy()
        for p in dst_pts.astype(int):
            cv2.circle(overlay, tuple(p), 8, (255,255,255), -1)
        for p in proj.astype(int):
            cv2.circle(overlay, tuple(p), 4, (128,128,128), -1)

        res_images.append(overlay)
        titles.append(f"transformed")
        
        showImages(res_images, titles)