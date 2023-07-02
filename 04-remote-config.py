"""Customizing your remote configuration.

rx gives you a lot of flexibility in terms of RAM, disk, CPU, and GPU options
on your remote machine. (Or, at least, it will!)

You can check out your current configuration by looking at .rx/remotes/default.
When you run `rx init`, rx uses that to provision a bog-standard Python 3.11
instance.

However, the files in .rx/remotes are simply starter templates and you can
create any configuration you want.

For example, this file uses removeprefix, which is a method added in Python
3.9. Try running this with Python 3.7 by creating a file `my-rx-configs/py37`
with the following content:

  {
    "image": {
      "docker": "python:3.7-slim"
    }
  }

Now tell rx that you want to use a different remote machine configuration by
running `rx init` again, this time with the --remote flag:

  $ rx init --remote=my-rx-configs/py37

Now if you run this script, you should see:

  $ rx python 04-remote-config.py
  Some Python projects:
  Traceback (most recent call last):
    File "04-remote-config.py", line 44, in <module>
      print(proj.removesuffix('Py'))
  AttributeError: 'str' object has no attribute 'removesuffix'

To upgrade back to Python 3.11, run `rx init` again without any flags and it'll
go back to using the config `default` is symlinked to. Now it prints:

  $ rx python 04-remote-config.py
  Some Python projects:
  Torch
  Pi
  Mongo

In the future these remote config files will be used to specify hardware
requirements, too.
"""

PY_PROJECTS = ['PyTorch', 'PyPi', 'PyMongo']
print('Some Python projects:')
for proj in PY_PROJECTS:
  print(proj.removeprefix('Py'))
