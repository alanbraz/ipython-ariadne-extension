# iPython Extension for WALA/ML a.k.a Ariadne 

This is a wrapper for [WALA/ML](https://wala.github.io/) that analyzes machine learning code using WALA inside an IPython notebook as an extension. It analyzes not only the running cells, but all the previous ones as a single source code and print the error in the cell's standard output.

### Overview 


### Installation

Inside a notebook, add this cell:

```python
# install
!pip install -I git+https://github.com/alanbraz/ipython-ariadne-extension.git
# Depending on the Jupyter permission you may need to add a --user option

# load extension
%load_ext ariadne
# to uninstall use %unload_ext
```

### Examples

Check the [ariadne-extension.ipynb](ariadne-extension.ipynb) notebook for a full test and examples.

Check demo notebook at Watson Studio: https://dataplatform.cloud.ibm.com/analytics/notebooks/b6ee33bd-8e56-4d8c-b95f-c0e9e392b9ee/view?access_token=561996ea008e91ef2c43ea0517e6bef00590e6ce447abc2ceca4da13074dd4c3
