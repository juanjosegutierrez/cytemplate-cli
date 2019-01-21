import argparse
import json
import sys
import time
from cytemplate.python_add import python_add
from cytemplate.cython_add import cython_add


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', type=int, default=5000,
                        help='the last number to add')
    args_dict = vars(parser.parse_args())

    t0 = time.time()
    cython_add(args_dict['number'])
    t1 = time.time()

    t2 = time.time()
    python_add(args_dict['number'])
    t3 = time.time()
    
    sys.stdout.write('Cython is {}x times faster.\n'.format((t3-t2)/(t1-t0)))


if __name__ == '__main__':
    main()
