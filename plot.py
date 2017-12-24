#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv(
        'data',
        sep='\s+',
        names=('x', 'y'),
        usecols=(0, 1),
    )
    df.plot(x='x', y='y', grid=True)
    plt.show()


if __name__ == '__main__':
    main()
