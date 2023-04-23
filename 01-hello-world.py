"""START HERE!

To start with, try running this script "normally":

    $ python 01-hello-world.py
    Hello world, I am ks-macbook-air.lan

This should print the name of your current local machine. To run this in the
cloud, add "rx" before the python command:

    $ rx python 01-hello-world.py
    Hello world, I am getting-started.rx

Congratulations, you just ran a command remotely! Try changing this script to
print "Goodbye from <hostname>" and running "rx python 01-hello-world.py"
again:

    $ rx python 01-hello-world.py
    Goodbye from getting-started.rx!

As you can see, the changes you made locally are immediately available on your
remote instance. You can run any other commands you want on your instance, just
prefix them with "rx":

    $ rx pwd
    $ rx 'ls -lh > ls-out'
    $ rx which python

Feel free to continue to experiment with this script or check out 02-output.py
for the next exercise.
"""
import socket

def main():
  print(f'Hello world, I am {socket.gethostname()}')

if __name__ == '__main__':
  main()
