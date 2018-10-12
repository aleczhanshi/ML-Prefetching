import os
from grammar import Grammar
import numpy as np


def isInt(s):
  try:
      int(s, 16)
      return True
  except ValueError:
      return False

def int2bits(x):
    return [int(b) for b in "{:064b}".format(int(x))]

def isData(line):
    return len(line) == 2 and isInt(line[0]) and isInt(line[1])

def convert_to_one_hot(array):
    array = np.array(array)
    print(array.shape)
    one_hot = np.zeros((array.size, array.max()+1), dtype=bool)
    one_hot[range(len(array)), array] = 1
    return one_hot

def preprocess(filename, FUTURE_WINDOW = 100):
    pc_in = []
    page_in = []
    page_out = []
    offset_in = []
    offset_out = []

    pc_dict = {}
    page_dict = {}

    addrs = []
    with open(filename, 'r') as fin:
        lines = fin.readlines()
        for i in range(len(lines)):
            trigger_line = lines[i].split()
            if isData(trigger_line):
                trigger_addr = trigger_line[1]
                addrs.append(trigger_addr)

    print('running sequitur')
    g = Grammar()
    g.train_string(addrs)
    print(g.print_grammar())

for filename in list(os.listdir(os.curdir)):
     if filename.endswith('txt'):
        print(filename)
        preprocess(filename.split(',')[0])
