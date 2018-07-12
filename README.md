# ipython-typecheck-extension

From this [tutorial](http://journalpanic.com/post/spice-up-thy-jupyter-notebooks-with-mypy/) that customizes IPython notebook with `magic` commands, this repo implements the same feature but using an [extension](http://ipython.readthedocs.io/en/stable/config/extensions/index.html).

In addition, it runs the `typecheck` not only at the current cell, but in **all previous cells that have run**. So if a variable is defined as integer in the first cell and you try to assign a string value to it in a second cell, it should fail.

### Installation

Inside a notebook, add this cell:

```python
# install
!pip install -I git+https://github.com/alanbraz/ipython-typecheck-extension.git
# Depending on the Jupyter permission you may need to add a --user option

# load extension
%load_ext typecheck
# to uninstall use %unload_ext
```

### Examples

Check the [typecheck-test.ipynb](typecheck-test.ipynb) notebook for a full test and examples.

Check demo notebook at Watson Studio: https://dataplatform.ibm.com/analytics/notebooks/56025e00-cfdd-4d84-a3ab-30ed95e7180c/view?access_token=83985d34b97207a63943a98c5237f0e0ef53a5edc4e1950bc48eea25e2e9f8cd
