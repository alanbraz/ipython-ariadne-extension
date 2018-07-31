"""Test Ariadne IPython extension."""
from ariadne import Ariadne
import IPython

def main():
    # # parse command line options
    # try:
    #     opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    # except getopt.error, msg:
    #     print msg
    #     print "for help use --help"
    #     sys.exit(2)
    # # process options
    # for o, a in opts:
    #     if o in ("-h", "--help"):
    #         print __doc__
    #         sys.exit(0)
    # # process arguments
    # for arg in args:
    #     process(arg) # process() is defined elsewhere
    ip = IPython.get_ipython()
    ml = Ariadne(ip)
    ml.check()

if __name__ == "__main__":
    main()
