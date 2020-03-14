import sys
from isOneToOne import *

# check for correct number of cli args
if len(sys.argv) != 3:
	sys.exit("Invalid number of arguments. Needs 2.")

# call function on cli args 2 and 3
if isOneToOne(sys.argv[1], sys.argv[2]):
	print("true")
else:
	print("false")
