"""Customizing your remote configuration.

rx gives you a lot of flexibility in terms of RAM, disk, CPU, and GPU options
on your remote machine.

You can check out your current configuration by looking at .rx/remotes/default.
When you run `rx init`, rx uses that to provision a bog-standard Python 3.11
instance.

However, the files in .rx/remotes are simply starter templates and you can
create any configuration you want.

For example, try running this file (04-remote-config.py) with the remote
instance you've been using so far. This file is valid Python 2 code, but not
Python 3, so You should see something like:

  $ rx python 04-remote-config.py
    File "/Users/k/gitroot/rx/samples/04-remote-config.py", line 14
      print "Hello from Python 2."
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

rx can pull any public docker image, so we'll create a remote machine with
Python 2. Create `.rx/remotes/python2-config` with the following contents:

  {
    "image": {
      "docker": "python:2.7.7"
    }
  }

Now tell rx that you want to use a different remote machine by running `rx init`
again:

  $ rx init --remote=python2-config

Now if you run this script, you should see:

  $ rx python 04-remote-config.py
  Hello from Python 2.

To switch back to Python 3, run `rx init` again without any flags and it'll go
back to using the config `default` is symlinked to.
"""

print "Hello from Python 2."
