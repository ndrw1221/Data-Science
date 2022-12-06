import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io, data


def fade_gradually(img):
    ''' fade color image to grayscale from left to right'''
    if img.shape[2] == 3:
        processed = img.copy()
    elif img.shape[2] == 4:  
        # convert rgba colorspace to rgb
        processed = skimage.color.rgba2rgb(img)

    
    processed = skimage.img_as_float(processed)
    processed_gray = skimage.color.rgb2gray(processed)
    # an rgb representation of the grayscale image
    processed_gray = skimage.color.gray2rgb(processed_gray)


    deg = 10  # degree of gradualness, higher number for smoother fading
    por = 0.5  # portion of fading to the whole image, ranges from 0 to 1
    seg = (processed.shape[1]*por) // deg  # segment for each fade
    weights = np.linspace(1, 0, deg)  # weight for each fade
    b = processed.shape[1]//2 - (processed.shape[1]*por)//2  # the begining of fading


    processed[:, int(b + deg*seg):] *= 0
    processed_gray[:, :int(b)] *= 0

    for i in range(deg):
        start = int(b + i*seg)
        end = int(start + seg)
        processed[:, start:end] *= weights[i]
        processed_gray[:, start:end] *= weights[-i-1]
    
    processed += processed_gray

    return processed


def image_matting(img):
    '''Remove background of an image, assuming all background is #000000.'''
    processed = img.copy()

    rgb_sum = np.sum(processed, axis=2)
    # pixels with r, g, b value sum under 15 will be set to transparent
    alpha = np.where(rgb_sum<15, 0, 255)
    processed = np.dstack((processed, alpha))

    return processed


def main():
    monkey_island = io.imread('monkey_island.jpg')
    cat = io.imread('cat.jpg')

    a = fade_gradually(monkey_island)
    b = image_matting(cat)
    

    plt.imshow(a)
    plt.show()
    plt.imshow(b)
    plt.show()

if __name__ == "__main__":
    main()


