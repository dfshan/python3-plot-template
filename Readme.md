# Introduction
This is a template about reading data with `pandas` and plotting data with `matplotlib`.

# Requirements

* python3
* tkinter (`python34-tkinter` package for Centos 7, `python3-tk` package for Ubuntu)
* Other packages in `requirements.txt`

## Install requirements in Centos 7

```shell
yum install python34 python34-tkinter
pip3 install -r requirements.txt
```

# Use customized paper style
1. Copy the style file `paper.mplstyle` into `mpl_configdir/stylelib`,
where `mpl_configdir` denotes the configdir of matplotlib.
`mpl_configdir` can be get by `matplotlib.get_configdir()`.
```shell
# In MacOS
mkdir -p ~/.matplotlib/stylelib/
cp paper.mplstyle ~/.matplotlib/stylelib/
```
2. Uncomment the line `plt.style.use('paper')` in `plot.py`
