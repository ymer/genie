#!/bin/env python

'''
usage:
 genie gsmr [options] <sum1> <sum2> <out>

options:
 --nojob             if front end
 --dry-run           dry run
 --threshold=T       GWAS threshold for inclusion [default: 5e-8]
 <bzx>               bzx input file. (Must end in .sumstats)
 <bzy>               bzy input file. (Must end in .sumstats)


'''

from docopt import docopt
import sys
sys.path.insert(1, sys.path[0] + '/../../library')
import md

arguments = docopt(__doc__)
if __name__ == '__main__':
    md.main(arguments,['gsmr'])

