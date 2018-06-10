a = [1,2,3,4]
b = [4,5,6,7]
xx = lambda x,y:x+y
print(xx(1,2))
print(list(map(lambda x,y: x+y,a,b)))