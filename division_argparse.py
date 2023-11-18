import argparse

mgs = "The Division ArgParser."
parser = argparse.ArgumentParser(description=mgs)

parser.add_argument('values', type=float, nargs=2, help='values to be divided', default=1)

parser.add_argument('-d','--Division', action='store_true', help='divide the values: v1/v2')

args = parser.parse_args()

print(args.values)

def division(v1, v2):
  return str(v1/v2)

if args.Division:
  print("The division: "+division(args.values[0], args.values[1]))
else:
  print("Command not received")
