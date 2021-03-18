import sys

def square_parameters(len):
	per = len*4
	sqr = len**2
	diag = round(len*pow(2,0.5),3)
	return (per,sqr,diag)


param = square_parameters(int(sys.argv[1]))
print('side of the square: ' + str(sys.argv[1]))
print('perimeter of the square: ' + str(param[0]))
print('square area: ' + str(param[1]))
print('diagonal of the square: ' + str(param[2]))

