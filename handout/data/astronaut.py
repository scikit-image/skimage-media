#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from skimage.data import astronaut


if __name__ == '__main__':
    # Save local copy of the Astronaut test image for use in LaTeX
    dpi = 100.0
    xpixels, ypixels = 512, 512

    # This yields a bit-perfect (512, 512) sized PNG with no margins
    fig = plt.figure(figsize=(ypixels / dpi, xpixels / dpi), dpi=dpi)
    fig.figimage(astronaut())
    fig.savefig('./astronaut.png')
