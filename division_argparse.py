import argparse

mgs = "The Division ArgParser."
parser = argparse.ArgumentParser(description=mgs)

parser.add_argument('value_v1', type=float, nargs='?', help='a value to be divided', default=0)
parser.add_argument('value_v2', type=float, nargs='?', help='a value to be the divisor', default=1)

parser.add_argument('-d','--Division',
                    help='divide the values: v1/v2')

args = parser.parse_args()

def division():
  return str(args.value_v1/args.value_v2)

if args.Division:
  print("The division: "+division())
else:
  print("Comand not received")
