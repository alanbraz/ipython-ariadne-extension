"""Experimental packege for IPython extension."""
import IPython
from .typecheck import TypeCheck
# from .autotime import timer
# from .typecheck_magic import TypeCheck as tcMagic

__version__ = "0.9"

def load_ipython_extension(ipython):
    # ipython.events.register('pre_run_cell', timer.start)
    # ipython.events.register('post_run_cell', timer.stop)
    tc = TypeCheck(ipython)
    ipython.events.register('post_run_cell', tc.check)
    # ipython.register_magics(tcMagic)

# def unload_ipython_extension(ipython):
    # ipython.events.unregister('pre_run_cell', timer.start)
    # ipython.events.unregister('post_run_cell', timer.stop)
    # ipython.events.unregister('pre_run_cell', tc.check)
