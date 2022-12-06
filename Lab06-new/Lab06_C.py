from skimage import img_as_float64, data
import numpy as np
import matplotlib.pyplot as plt


def my_resize(img, height, width):
    """
    Resize an image to a given heigth and width using bilinear interpolation.
    """
    img = img_as_float64(img)
    # the last row and column (rightmost and bottommost)
    l_row = img[-1]
    l_col = img[:, -1]

    x = np.linspace(0, img.shape[0] - 1, height)[:-1][:, np.newaxis]
    x1 = x.astype(int)
    x2 = x1 + 1

    y = np.linspace(0, img.shape[1] - 1, width)[:-1]
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

    processed = (
        ((y2 - y) * (x2 - x)) * q11
        + ((y2 - y) * (x - x1)) * q21
        + ((y - y1) * (x2 - x)) * q12
        + ((y - y1) * (x - x1)) * q22
    )
    l_col = c1 * (x2 - x) + c2 * (x - x1)
    l_row = r1 * (y2 - y) + r2 * (y - y1)
    l_row = np.append(l_row, img[-1, -1])

    processed = np.hstack((processed, l_col))
    processed = np.vstack((processed, l_row))

    return processed


def my_rotation(img, angle):
    """
    Rotate an rgb image to any angle in degree.
    Positive value of angle for CCW rotation and negative value of angle for CW rotation.

    """
    angle = np.deg2rad(angle)

    h, w, d = img.shape
    cx, cy = (h // 2, w // 2)

    rot_img_height = round(abs(h * np.sin(angle))) + round(abs(w * np.cos(angle)))
    rot_img_width = round(abs(w * np.cos(angle))) + round(abs(h * np.sin(angle)))

    processed = np.uint8(np.zeros((rot_img_height, rot_img_width, d)))
    mid_x, mid_y = (rot_img_width // 2, rot_img_height // 2)

    for i in range(rot_img_height):
        for j in range(rot_img_width):
            x = (i - mid_x) * np.cos(angle) + (j - mid_y) * np.sin(angle)
            y = -(i - mid_x) * np.sin(angle) + (j - mid_y) * np.cos(angle)
            x = round(x) + cy
            y = round(y) + cx

            if (0 <= x < h) and (0 <= y < w):
                processed[i, j, :] = img[x, y, :]

    return processed


def main():
    camera_resized = my_resize(data.camera(), 300, 1000)
    plt.imshow(camera_resized, cmap="gray")
    plt.show()

    camera_rotated = my_rotation(data.astronaut(), -135)
    plt.imshow(camera_rotated, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
