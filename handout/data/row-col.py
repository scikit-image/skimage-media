#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(3, 1.5))

    # Set up grid plot
    ax.set_xlim(0, 6)
    ax.set_ylim(3, 0)
    ax.xaxis.set_major_locator(MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(MultipleLocator(0.2))
    ax.yaxis.set_major_locator(MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))
    ax.grid(which='major', axis='x', linewidth=.75, linestyle='-', color='.8')
    ax.grid(which='minor', axis='x', linewidth=.25, linestyle='-', color='.8')
    ax.grid(which='major', axis='y', linewidth=.75, linestyle='-', color='.8')
    ax.grid(which='minor', axis='y', linewidth=.25, linestyle='-', color='.8')

    # Turn off tick labels/markers
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Remove axes
    for side in ['bottom', 'right', 'top', 'left']:
        ax.spines[side].set_visible(False)

    # Label appropriately
    ax.set_ylabel('Rows')
    ax.set_xlabel('Columns', labelpad=9)
    ax.xaxis.set_label_position('top')

    # Generate arrows
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height

    hw = 1./20. * (ymax-ymin)
    hl = 1./20. * (xmax-xmin)
    lw = 1.    # axis line width
    ohg = 0.3  # arrow overhang
    yhw = hw / (ymax-ymin) * (xmax-xmin) * height/width
    yhl = hl / (xmax-xmin) * (ymax-ymin) * width/height

    ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw=lw,
             head_width=1.3 * yhw, head_length=-1 * yhl, overhang=ohg,
             length_includes_head=False, clip_on=False, zorder=9)

    ax.arrow(0, ymax, 0., -1 * (ymax-ymin), fc='k', ec='k', lw=lw,
             head_width=1. * yhw, head_length=-1 * yhl, overhang=ohg,
             length_includes_head=False, clip_on=False, zorder=10)

    # Save the result
    fig.tight_layout()
    fig.savefig('./row-col.png', dpi=250)
