import sys
from os import rename, listdir

fnames = listdir('.')

print 'fnames are: ', fnames

counter = 1

fn = raw_input('Enter YYYYMMDD_name: ')
fnew = fn

for fname in fnames:
  if fname != 'renamer.py':
    nname = fnew + str(counter)
    rename(fname, nname)
    counter += 1

print 'complete!'

