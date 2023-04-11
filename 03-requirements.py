"""How to use Python dependencies with rx.

This script imports two packages: absl and art. If you take a look at
requirements.txt in this directory, you'll see that it defines absl-py (which
makes "absl" available), but not the art package.

To start, try running this script with rx:

    $ rx python 03-requirements.py 'more cowbell'

You'll see a big stacktrace, because "art" isn't found.

rx uses your requirements.txt to figure out which packages to install on the
remote machine. Thus, to install the art package remotely, open up
requirements.txt (locally) and add a line:

art==5.8

Then save requirements.txt and go back to the command line. Try running this
script again and now rx has all of the packages it needs:

    $ rx python 03-requirements.py 'more cowbell'
                                                           _            _  _
     _ __ ___    ___   _ __   ___    ___   ___  __      __| |__    ___ | || |
    | '_ ` _ \  / _ \ | '__| / _ \  / __| / _ \ \ \ /\ / /| '_ \  / _ \| || |
    | | | | | || (_) || |   |  __/ | (__ | (_) | \ V  V / | |_) ||  __/| || |
    |_| |_| |_| \___/ |_|    \___|  \___| \___/   \_/\_/  |_.__/  \___||_||_|

Note that you did not even need to install the package locally (although you
could): rx took care of installing packages on the remote machine for you based
on the contents of requirements.txt.
"""

from absl import app
import art

def main(argv):
  if len(argv) != 2:
    print('You must pass in a string to print.')
  art.tprint(argv[1])

if __name__ == '__main__':
  app.run(main)
