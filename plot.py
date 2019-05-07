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
        'linestyle': '-',
        'marker': 'o',
        'markevery': 1,
        'markersize': 12,
        'markerfacecolor': 'None',
    },
    {
        'color': '#00a000',
        'linestyle': '-',
        'marker': 'x',
        'markevery': 1,
        'markerfacecolor': 'None',
    },
    {
        'color': '#5060d0',
        'linestyle': '-',
        'marker': '>',
        'markersize': 12,
        'markevery': 1,
    },
    {
        'color': '#f25900',
        'linestyle': '-',
        'marker': '+',
        'markevery': 1,
        'markersize': 12,
        'markerfacecolor': 'None',
    },
    {
        'color': '#500050',
        'linestyle': '-',
        'marker': '*',
        'markevery': 1,
        'markersize': 20,
    }
]


def get_cdf(data):
    data_sorted = np.sort(data)
    n = len(data)
    prob = np.arange(1, n + 1) / n
    return data_sorted, prob


def plot_cdf(data, axis, **kwargs):
    ''' Plot CDF (Cumulative Distribution Function)
    Args:
        data: A list of data for plotting CDF
        axis: A matplotlib.axes.Axes object
        kwargs: Other arguments for matplotlib.axes.Axes.step
    '''
    x_values, cdf = get_cdf(data)
    return axis.step(x_values, cdf, where='post', **kwargs)


def draw_vertical_broken_ax(fig, ax1, ax2, xlabel=None, ylabel=None):
    ax1.spines['right'].set_visible(False)
    ax1.yaxis.tick_left()
    ax2.spines['left'].set_visible(False)
    ax2.yaxis.tick_right()

    # Draw the diagonal lines
    d = .015
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax1.transAxes, color='#808080', clip_on=False)
    ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # bottom-right diagonal
    ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # top-right diagonal
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax2.transAxes, color='#808080', clip_on=False)
    ax2.plot((-d, +d), (-d, +d), **kwargs)  # bottom-right diagonal
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # top-right diagonal
    fig.subplots_adjust(wspace=0.1, bottom=0.15, left=0.18)

    if xlabel is not None:
        fig.text(0.5, 0.04, xlabel, ha='center')
    if ylabel is not None:
        ax1.set_ylabel(ylabel)


def example_broken_axis():
    matplotlib.rcParams['figure.autolayout'] = False
    x_vals = np.linspace(1, 10, 100)
    y_vals = np.sin(x_vals)
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    lstyle = styles[0]
    lstyle['marker'] = None
    line = ax1.plot(x_vals, y_vals, **lstyle)[0]
    ax2.plot(x_vals, y_vals, **lstyle)
    ax1.set_xlim(1, 5)
    ax2.set_xlim(6, 10)
    draw_vertical_broken_ax(fig, ax1, ax2, xlabel='x val', ylabel='y val')
    ax1.minorticks_on()
    ax1.grid(axis='both', which='major', ls='dotted', linewidth=2, alpha=0.8)
    ax1.grid(axis='both', which='minor', ls='dotted', linewidth=1.5, alpha=0.5)
    ax2.minorticks_on()
    ax2.grid(axis='both', which='major', ls='dotted', linewidth=2, alpha=0.8)
    ax2.grid(axis='both', which='minor', ls='dotted', linewidth=1.5, alpha=0.5)
    fig.legend(
        handles=(line, ),
        labels=('line 1', ),
        loc='center',
    )
    plt.show()


def example_cdf(fname=None):
    if fname is None:
        data = np.geomspace(1, 100, 10000)
    else:
        data = np.loadtxt(fname)
    plt.style.use('paper')
    fig, ax = plt.subplots()
    lstyle = styles[0]
    lstyle['markevery'] = 1000
    plot_cdf(data, ax, label='line1', **lstyle)
    # set grid styles
    ax.minorticks_on()
    ax.grid(axis='both', which='major', ls='dotted', linewidth=2, alpha=0.9)
    ax.grid(axis='both', which='minor', ls='dotted', linewidth=1.5, alpha=0.5)
    ax.set_xscale('log')
    plt.legend(loc='best')
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
        ax.plot(df.iloc[:, 0], df.iloc[:, idx], **styles[idx-1])
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
    usage = 'USAGE: %s [cdf [FILE] | broken-axis]' % sys.argv[0]
    if len(sys.argv) == 1:
        example()
    elif len(sys.argv) >= 2 and sys.argv[1] == 'cdf':
        if len(sys.argv) == 2:
            example_cdf(None)
        else:
            example_cdf(sys.argv[2])
    elif len(sys.argv) >= 2 and sys.argv[1] == 'broken-axis':
        example_broken_axis()
    else:
        print(usage)
