import argparse
from functools import reduce
import operator


def sum_list(args):
    value = 0
    for arg in args:
        value += reduce(operator.add,map(int,arg.split(" ")))
    return value

parser = argparse.ArgumentParser()
 
parser.add_argument('my_list', 
                    metavar='N', 
                    type=str, 
                    nargs='+',
                    help='a list of strings')

parser.add_argument(dest='accumulate', 
                    action='store_const',
                    const=sum_list, 
                    help='sum list of strings')
 
args = parser.parse_args()
print(args.accumulate(args.my_list))