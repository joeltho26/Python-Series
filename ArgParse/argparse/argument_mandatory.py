import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--string1', type=str, required=True)
parser.add_argument('--string2', type=str)
args = parser.parse_args()

if args.string2:
	print(args.string1, args.string2)
else:
	print(args.string1)