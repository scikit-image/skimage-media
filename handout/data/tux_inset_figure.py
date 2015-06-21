#!/usr/bin/env python
import numpy as np
import skimage.io
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid.inset_locator import mark_inset


def _determine_ideal_value(imval, ma=255):
    if imval > 0.5 * ma:
        shade = 0.15
    else:
        shade = 0.85
    return str(shade)


def overlay_numbers(axis, array, extent, subextent, *args, **kwargs):
    axis.imshow(array, extent=extent, *args, **kwargs)
    if array.ndim > 2:
        from skimage.color import rgb2gray
        array = rgb2gray(array)
        array *= 255
        array = array.round().astype(np.uint8)

    slices = [slice(subextent[0], subextent[1]),
              slice(subextent[2], subextent[3])]
    for i, r in enumerate(np.flipud(array).T[slices]):
        for j, c in enumerate(r):
            axis.text(i + subextent[0] + 0.5, j + subextent[2] + 0.5, c,
                      weight='demibold',
                      horizontalalignment='center',
                      verticalalignment='center',
                      color=_determine_ideal_value(c, ma=array.max()))


if __name__ == '__main__':
    tux = skimage.io.imread('./tux_icon-33px.png')

    fig, ax = plt.subplots(figsize=(5, 5))

    extent0 = [0, 33, 0, 36]
    ax.imshow(tux, extent=extent0, interpolation='nearest')
    axins = zoomed_inset_axes(ax, 3.4, loc=3)
    extent1 = [18, 23, 18, 23]
    overlay_numbers(axins, tux, extent0, extent1, interpolation='none')
    axins.set_xlim(*extent1[:2])
    axins.set_ylim(*extent1[2:])
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    ax.axis('off')
    fig.tight_layout()
    fig.savefig('./tux_inset.png', dpi=150)

    # plt.show()
