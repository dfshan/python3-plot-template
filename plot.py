#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# line styles
styles = [
    {
        'color': '#a00000',
        'ls': '-',
        'marker': 'o',
        'markevery': 1,
        'markersize': 12,
        'markerfacecolor': 'None',
    },
    {
        'color': '#00a000',
        'ls': '-',
        'marker': 'x',
        'markevery': 1,
        'markerfacecolor': 'None',
    },
    {
        'color': '#5060d0',
        'ls': '-',
        'marker': '>',
        'markersize': 12,
        'markevery': 1,
    },
    {
        'color': '#f25900',
        'ls': '-',
        'marker': '+',
        'markevery': 1,
        'markersize': 12,
        'markerfacecolor': 'None',
    },
    {
        'color': '#500050',
        'ls': '-',
        'marker': '*',
        'markevery': 1,
        'markersize': 20,
    }
]


def example_cdf(fname=None):
    if fname is None:
        data = np.geomspace(1, 100, 10000)
    else:
        data = np.loadtxt(fname)
    plt.style.use('paper')
    fig, ax = plt.subplots()
    hist_style = {
        'color': '#a00000',
        'ls': '-',
        'linewidth': 3,
    }
    n, bins, patches = plt.hist(
        data, density=1, cumulative=True,
        histtype='step', bins=len(data),
        label='line1',
        **hist_style,
    )
    patches[0].set_xy(patches[0].get_xy()[:-1])
    # set legend to line
    handles, labels = ax.get_legend_handles_labels()
    new_handles = [matplotlib.lines.Line2D([], [], c=h.get_edgecolor())
                   for h in handles]
    ax.minorticks_on()
    ax.grid(axis='both', which='major', ls='dotted', linewidth=2, alpha=0.9)
    ax.grid(axis='both', which='minor', ls='dotted', linewidth=1.5, alpha=0.5)
    ax.legend().set_visible(False)
    ax.set_xscale('log')
    plt.legend(handles=new_handles, labels=labels, loc='best')
    plt.xlabel('x val')
    plt.ylabel('y val')
    plt.tight_layout()
    plt.show()


def example():
    df = pd.read_csv(
        'data.csv',
        sep=r'\s+',
        header=None,
    )
    # plt.style.use('paper')
    fig, ax = plt.subplots()
    idx = 1
    while idx < df.shape[1]:
        ax.plot(df.iloc[:,0], df.iloc[:,idx], **styles[idx-1])
        idx += 1
    ax.minorticks_on()
    ax.grid(axis='both', which='major', ls='dotted', linewidth=2, alpha=0.9)
    ax.grid(axis='both', which='minor', ls='dotted', linewidth=1.5, alpha=0.5)
    ax.legend(loc='best', ncol=3)
    plt.xlabel('x val')
    plt.ylabel('CDF')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        example()
    elif len(sys.argv) >= 2 and sys.argv[1] == 'cdf':
        if len(sys.argv) == 2:
            example_cdf(None)
        else:
            example_cdf(sys.argv[2])
