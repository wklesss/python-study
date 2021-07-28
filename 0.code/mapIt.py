#! python
# mapIt.py - launches a map in the brower using an address from the 
# command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])

# TODO:Get address from clipboard.