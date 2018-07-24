"""Ariadne IPython extension."""
import IPython
from .ariadne import Ariadne

__version__ = "1.0"

def load_ipython_extension(ipython):
    ml = Ariadne(ipython)
    ipython.events.register('post_run_cell', ml.check)
