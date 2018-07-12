"""source: https://github.com/cpcloud/ipython-autotime."""
from __future__ import print_function
from IPython.core.magics.execution import _format_time as format_delta
import time


class LineWatcher(object):
    """
    Class that implements a basic timer.
    """
    def __init__(self):
        self.start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        stop_time = time.time()
        if self.start_time:
            diff = stop_time - self.start_time
            assert diff > 0
            print('time: {}'.format(format_delta(diff)))


timer = LineWatcher()
