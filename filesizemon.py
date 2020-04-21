#!/usr/bin/env python3
# Usage Example: sizemon.py '/var/log/apache2/*access*log'
# MAKE SURE YOU USE single quotes around path/pattern specification
# If you dont use the single quotes, current script version will monitor only
# the first bash-expanded filename.
#
# Author: Buanzo
# License: GPLv3
# Version: 0.1
# Date: 4/21 [I was busy 4/20]
#
# THIS IS A QUICK AND DIRTY SCRIPT FULL OF BAD CODE
#
import glob
import sys
import os
import time
from pprint import pprint

bc = float(0)
bc_item = ''


def get_change_stats(item, current, previous):
  global bc
  global bc_item
  bn = os.path.basename(item)
  if current == previous:
    x = '{:50}\tCUR={:10}\tORIG={:10}\tCHANGE=0%'.format(bn, current, previous)
  else:
    change_percent = ((float(current)-previous)/previous)*100
    if change_percent > bc:
      bc = change_percent
      bc_item = item
    x = '{:50}\tCUR={:10}\tORIG={:10}\tCHANGE={:f}%'.format(bn,
                                                            current,
                                                            previous,
                                                            change_percent)
  return(x)


def logsizemon():
  try:
    pat = sys.argv[1]
  except Exception:
    print("Usage EXAMPLE: {} '/logs/*.log'".format(sys.argv[0]))
    sys.exit(1)

  i_sizes = {}
  c_sizes = {}

  # load initial file sizes
  print('Loading initial sizes...')
  for f in glob.glob(sys.argv[1]):
    i_sizes[f] = os.path.getsize(f)

  # Initial wait
  print('Waiting 10 seconds to begin monitoring...')
  time.sleep(10)

  while True:
    # Get current file sizes
    for f in glob.glob(sys.argv[1]):
      # FIX: Include newly appeared files
      c_sizes[f] = os.path.getsize(f)
    print("\033[2J\033[0;0H\033[0;37m")  # ANSI ftw
    for item in i_sizes:
      current = c_sizes[item]
      previous = i_sizes[item]
      print(get_change_stats(item, current, previous))
    print("\033[1;33m------------------------------------------\033[0;37m")
    print("\033[1;32mMAX CHANGE: {:f}% for {}\033[0;37m".format(bc,
                                                                bc_item))
    time.sleep(10)


if __name__ == '__main__':
  logsizemon()
