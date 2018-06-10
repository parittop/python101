import csv

def readdata():
	with open('data.csv', newline='') as f:
		fr = csv.reader(f)
		#fw = csv.writer(f)
		#print(type(fr))
		for i,j,k in fr:
			print('product: {} price: {:.2f} quantity: {}'.format(i,float(j),k))
	 

def writedata():
	with open('data.csv','a',newline='') as f:
		fw = csv.writer(f)
		dt = ['Pepsi',18,150]
		fw.writerow(dt)
		print('data was written')

writedata()
readdata()