import skimage
from skimage import io, transform, filters
import numpy as np
import matplotlib.pyplot as plt

def scan_document(img):
    
    img = img.copy()

    src = np.array([[0, 0], [400, 0], [0, 800], [400, 800]])
    dst = np.array([[120, 178],  # upper left
                    [275, 170],  # upper right
                    [63, 527],  # bottom left
                    [310, 532]])  # bottom right

    tform3 = transform.ProjectiveTransform()
    tform3.estimate(src, dst)

    warped = transform.warp(img, tform3, output_shape=(800, 400))

    warped_gray = skimage.color.rgb2gray(warped)

    window_size = 25
    thresh_sauvola = filters.threshold_sauvola(warped_gray, window_size=window_size, k=0.1)
    scanned = warped_gray > thresh_sauvola

    return scanned


def main():
    img = io.imread('invoice.jpg')
    scanned = scan_document(img)
    plt.imshow(scanned, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()
    
    