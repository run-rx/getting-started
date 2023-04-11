"""Accessing output files from rx.

You may want access to artifacts that your program produces: binaries, images,
models, etc. As long as they are created in the rx root directory (the
directory containing .rx), then they are automatically synced back to your
client.

For example, first try running this script locally, which creates an output
file at child1/child2/my-output.txt:

  $ python 02-io.py
  Wrote child1/child2/my-output.txt

If you run `ls`, you can see that there's a new directory in this folder:
child1.

Now try running this on rx:

  $ rx python 02-io.py
  Wrote child1/child2/my-output.txt

When rx finishes, it "sweeps" any outputs that were created into a directory
called rx-out. It'll also print all output files.

So now you can see your original output file is still in
child1/child2/my-output.txt and the rx output is in
rx-out/child1/child2/my-output.txt.
"""
import datetime
import pathlib

def main():
  output_dir = pathlib.Path('child1/child2')
  output_dir.mkdir(parents=True, exist_ok=True)
  out_file = output_dir / 'my-output.txt'
  with out_file.open(mode='wt', encoding='utf-8') as fh:
    fh.write(f'Here is some output: {datetime.datetime.now()}')
  print(f'Wrote {out_file}')

if __name__ == '__main__':
  main()
