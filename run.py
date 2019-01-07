#!/usr/bin/env python
#
from __future__ import print_function
from __future__ import division
from __future__ import with_statement

import os,argparse,logging
import importlib
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run project euler problem")
    parser.add_argument("-p", "--problem", type=int, required=True, help="the problem number")
    parser.add_argument("--test", action='store_true', default=False, help="run the test")
    parser.add_argument('-v', '--verbosity', type=int, default=0, help='verbosity level for debug')
    args = parser.parse_args()

    if args.verbosity > 1:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.verbosity > 0:
        logging.info(args)

    mymodule = 'p{:03d}'.format(args.problem)
    mycode = mymodule+'.py'
    if not os.path.isfile(mycode):
        raise NotImplementedError('Problem {} is not implemented.'.format(args.problem))

    logger = logging.getLogger(mymodule)
    fh = logging.FileHandler('{}.log'.format(mymodule))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    module = importlib.import_module(mymodule, package=None)
    ts1 = time.time()
    module.main(args)
    if args.verbosity > 0:
        ts2 = time.time()
        logging.info("Run time:{} second".format(ts2-ts1))
