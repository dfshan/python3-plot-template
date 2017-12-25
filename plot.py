#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

# line styles
styles=[
    {
        'color': '#a00000',
        'ls' : '-',
        'marker' : 'o',
        'markevery' : 1,
        'markersize' : 12,
        'markerfacecolor' : 'None',
    },
    {
        'color': '#00a000',
        'ls' : '-',
        'marker' : 'x',
        'markevery' : 1,
        'markerfacecolor' : 'None',
    },
    {
        'color': '#5060d0',
        'ls' : '-',
        'marker' : '>',
        'markersize' : 12,
        'markevery' : 1,
    },
    {
        'color': '#f25900',
        'ls' : '-',
        'marker' : 'd',
        'markevery' : 3,
        'markerfacecolor' : 'None',
    },
    {
        'color': '#500050',
        'ls' : '*',
        'marker' : 'd',
        'markevery' : 1,
        'markerfacecolor' : 'None',
    }
]

def main():
    df = pd.read_csv(
        'data',
        sep='\s+',
        names=('x', 'y'),
        usecols=(0, 1),
    )
    #plt.style.use('paper')
    df.plot(x='x', y='y', **styles[0])
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
