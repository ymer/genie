#!/bin/env python

'''
usage:
 gcta variance --grm=GRMFILE --pheno=FILE [options]

options:
 --pheno=FILE          plink format pheno file
 --mpheno=NUMBER       if multiple phenotypes in pheno file, specify which one to use
 --grm=GRMFILE         grm file
 --out=PREFIX          outname prefix [default: variance_out]
 --keep=FILE           list file
 --reml-priors=N1      two numbers
 --reml-alg=NUMBER     0(AI) or 1(AI) or 2(EM)
 --reml-no-constrain   allow negative
 --reml-maxit=NUMBER   maximum number of iterations
 --gxe                 test gxe
 --covar=FILE          covariate file
 --qcovar=FILE         quantitative covariate file
 --reml-lrt=NUMBER     see GCTA doc
 --reml-no-lrt         turn off the LRT
 --prevalence=NUMBER   prevalence of the disease
 --dry-run             show only the code
 --nojob               front end

'''

from docopt import docopt
import sys
sys.path.insert(1, sys.path[0] + '/../../../library')
import md
from md import process_list

arguments = docopt(__doc__)
if __name__ == '__main__':
    md.main(arguments,['variance'])