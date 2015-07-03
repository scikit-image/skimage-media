#!/usr/bin/env python
import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import blob_doh
from skimage.color import rgb2gray


if __name__ == '__main__':

    image = data.hubble_deep_field()[0:330, 200:500]
    image_gray = rgb2gray(image)

    blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)

    fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(3.8, 2))
    ax0.imshow(image, interpolation='nearest')
    ax1.imshow(image, interpolation='nearest')
    for blob in blobs_doh:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='red', linewidth=1.5, fill=False)
        ax1.add_patch(c)

    ax0.axis('off')
    ax1.axis('off')
    fig.subplots_adjust(0, 0, 1, 1, 0.075, 0)
    fig.savefig('./doh_galaxies.png', dpi=250)
