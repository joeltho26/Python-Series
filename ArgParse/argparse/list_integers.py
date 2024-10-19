import argparse

def list_of_ints(arg):
	return list(map(int, arg.split(',')))

parser = argparse.ArgumentParser()
parser.add_argument('--int-list', type=list_of_ints)
args = parser.parse_args()
print(args.int_list)