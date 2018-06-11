import numpy
inp=input()
new=map(float,inp.split())
new=list(new)
arr = numpy.array(new)
print(arr)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
