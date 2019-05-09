# Introduction
This is a template about reading data with `pandas` and plotting data with `matplotlib`.

# Requirements

* `python3`
* `tkinter` (`python34-tkinter` package for Centos 7, `python3-tk` package for Ubuntu, `python-pmw` package for Arch Linux)
* Other packages in `requirements.txt`
* `LaTeX`

## Install requirements in Centos 7

``` bash
yum install python34 python34-tkinter
pip3 install -r requirements.txt
```

# Use customized paper style
## Option 1:
``` bash
ln -s paper.mplstyle matplotlibrc
```

## Option 2:
1. Copy the style file `paper.mplstyle` into `mpl_configdir/stylelib`,
where `mpl_configdir` denotes the configdir of matplotlib.
`mpl_configdir` can be get by `matplotlib.get_configdir()`.
``` bash
# In MacOS
mkdir -p ~/.matplotlib/stylelib/
cp paper.mplstyle ~/.matplotlib/stylelib/
```
2. Uncomment the line `plt.style.use('paper')` in `plot.py`
