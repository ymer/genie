#!/bin/env python

'''

usage:
 eqtl fusion [options] --sumstats=FILE 

options:
 --sumstats=FILE       summary statistics file or .list 
 --weights=FILE        gene expression weights file or .list [default: |resources/fusion/weights.list]
 --chr=NUMBER          chromosome number
 --out=PREFIX          output prefix [default: genie_fusion]
 --nojob               nojob
 --dry-run             dry run
 
'''

from docopt import docopt
import sys
sys.path.insert(1, sys.path[0] + '/../../../library')
import md
from md import process_list

arguments = docopt(__doc__)
if __name__ == '__main__':
    md.main(arguments,['fusion'])