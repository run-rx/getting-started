"""Accessing output files from rx.

You may want access to artifacts that your program produces: binaries, images,
models, etc. As long as they are created under the rx root directory (the
directory where you ran "rx init"), then they will be automatically synced back
to your client.

For example, try redirecting output to a file under rx-out:

  $ rx 'date > my-date'
  Changed:
    my-date

Note the quotes around the command: if you do not quote it, your local shell
will grab the redirect before it can be sent to the remote machine!

Try running this script on rx:

  $ rx python 02-output.py
  Wrote timestamps/now.txt
  Changed:
    timestamps/now.txt

Note that the remote directory is reset to exactly mirror your local machine
before each command (and your local directory will be synced to mirror the
remote at the end of each command).
"""
import datetime
import pathlib

def main():
  output_dir = pathlib.Path('timestamps')
  output_dir.mkdir(parents=True, exist_ok=True)
  out_file = output_dir / 'now.txt'
  with out_file.open(mode='wt', encoding='utf-8') as fh:
    fh.write(
      f'At the sound of the beep, the time is: {datetime.datetime.now()}')
  print(f'Wrote {out_file}')

if __name__ == '__main__':
  main()
