#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

from skimage.transform import hough_line, hough_line_peaks
from skimage.draw import line_aa


if __name__ == '__main__':
    # Construct test image
    image = np.zeros((200, 100))

    # Line 0
    rr, cc, val = line_aa(50, 15, 140, 97)
    image[rr, cc] = val

    # Line 1
    rr, cc, val = line_aa(100, 5, 12, 84)
    image[rr, cc] = np.fmax(image[rr, cc], val)

    # Line 2
    rr, cc, val = line_aa(140, 15, 160, 80)
    image[rr, cc] = np.fmax(image[rr, cc], val)

    # Compute the Hough transform for display
    h, theta, d = hough_line(image)

    fig, ax = plt.subplots(1, 3, figsize=(6, 3.5))

    # Original image
    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].axis('off')

    # Display Hough transform
    ax[1].imshow(np.log(1 + h),
                 extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]),
                         d[-1], d[0]],
                 cmap=plt.cm.gray, aspect=1 / 1.5)
    ax[1].axis('off')

    # Original image with lines detected
    ax[2].imshow(image, cmap=plt.cm.gray)
    rows, cols = image.shape
    for _, angle, dist in zip(*hough_line_peaks(h, theta, d, min_angle=5,
                                                min_distance=5)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - cols * np.cos(angle)) / np.sin(angle)
        ax[2].plot((0, cols), (y0, y1), '-r')
    ax[2].axis((0, cols, rows, 0))
    ax[2].axis('off')

    # Save a nice figure
    fig.tight_layout()
    fig.subplots_adjust(wspace=0, left=0, right=1, top=1, bottom=0)
    fig.savefig('./hough_lines.png', dpi=300)
