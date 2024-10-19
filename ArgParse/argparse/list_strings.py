import argparse

def list_of_strings(arg):
	return arg.split(',')

parser = argparse.ArgumentParser()
parser.add_argument('--str-list', type=list_of_strings)
args = parser.parse_args()
print(args.str_list)