import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io, img_as_float, data


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


def my_resize(img, height, width):
    '''Resize image to given heigth and width. Implementing 
       bilinear interpolation.
    '''
    img = img_as_float(img)
    # the last row and column (rightmost and bottommost)
    l_row = img[-1]
    l_col = img[:, -1]
    
    x = np.linspace(0, img.shape[0]-1, height)[:-1][:, np.newaxis]
    x1 = x.astype(int)
    x2 = x1 + 1
    
    y = np.linspace(0, img.shape[1]-1, width)[:-1]
    y1 = y.astype(int)
    y2 = y1 + 1
    
    q11 = img[x1, y1]
    q21 = img[x2, y1]
    q12 = img[x1, y2]
    q22 = img[x2, y2]
    
    c1 = l_col[x1]
    c2 = l_col[x2]
    r1 = l_row[y1]
    r2 = l_row[y2]
    
    processed = (((y2-y)*(x2-x))*q11 +
              ((y2-y)*(x-x1))*q21 +
              ((y-y1)*(x2-x))*q12 +
              ((y-y1)*(x-x1))*q22) 
    l_col = c1*(x2-x)+c2*(x-x1)
    l_row = r1*(y2-y)+r2*(y-y1)
    l_row = np.append(l_row, img[-1, -1])
    
    processed = np.hstack((processed, l_col))
    processed = np.vstack((processed, l_row))
    
    return processed


def main():
    mkilnd = io.imread('monkey_island.jpg')
    cat = io.imread('cat.jpg')
    camera = data.camera()

    a = fade_gradually(mkilnd)
    b = image_matting(cat)
    c = my_resize(camera, 300, 800)

    plt.imshow(a)
    plt.show()
    plt.imshow(b)
    plt.show()
    plt.imshow(c, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()


