#!/usr/bin/env python
from skimage.data import astronaut
import skimage.io


if __name__ == '__main__':
    # Save local copy of the Astronaut test image for use in LaTeX
    skimage.io.imsave('./astronaut.png', astronaut())
