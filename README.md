# iPython Extension for WALA/ML a.k.a Ariadne

This is a wrapper for [WALA/ML](https://wala.github.io/) that analyzes machine learning code using WALA inside an IPython notebook as an extension. It analyzes not only the running cells, but all the previous ones as a single source code and print the error in the cell's standard output.

### Overview

![overview](https://raw.githubusercontent.com/alanbraz/ipython-ariadne-extension/master/oeverview.png)

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

Check demo notebook at Watson Studio: https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/cd3bafe8-b817-46a3-a0d7-7ffbd55b4796/view?access_token=2b24ea38ca6697ede1e05a22433ca4ae601c9b37dac131bac27f8d4ef54a9e42
