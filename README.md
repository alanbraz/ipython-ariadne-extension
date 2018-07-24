# ipython-ariadne-extension

This is a wrapper for [WALA/ML](https://github.com/wala/ML) that analyzes machine learning code using WALA inside an IPython notebook as an extension. It analyzes not only the running cells, but all the previous ones as a single source code and print the error in the cell's standard output.


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

### Example

Check the [ariadne-test.ipynb](ariadne-test.ipynb) notebook for a full test and examples.

Check demo notebook at Watson Studio: https://dataplatform.ibm.com/analytics/notebooks/56025e00-cfdd-4d84-a3ab-30ed95e7180c/view?access_token=83985d34b97207a63943a98c5237f0e0ef53a5edc4e1950bc48eea25e2e9f8cd
