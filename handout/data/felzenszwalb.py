#!/usr/bin/env python
import matplotlib.pyplot as plt

from skimage.data import astronaut
from skimage.segmentation import felzenszwalb, mark_boundaries
from skimage.util import img_as_float

if __name__ == '__main__':
    img = img_as_float(astronaut())
    segments_fz = felzenszwalb(img, scale=600, sigma=1, min_size=50)

    fig, ax = plt.subplots(figsize=(5, 5))
    fig.subplots_adjust(0, 0, 1, 1, 0, 0)

    ax.imshow(mark_boundaries(img, segments_fz, color=(0, 1, 0)),
              interpolation='none')
    ax.axis('off')

    fig.savefig('./felzenszwalb.png', dpi=200)
