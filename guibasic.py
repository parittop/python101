from tkinter import *
from tkinter import ttk

def cal():
	bts = float(btsPrice.get())
	station = float(totalStation.get())
	#print('bts fare:', bts*station)  
	totalFare.set("{:,.2f}".format(bts*station)) 

gui=Tk()
gui.geometry('500x500+0+0')
gui.title('my first python app')

totalStation=StringVar()
btsPrice=StringVar()
totalFare=StringVar()

l1 = ttk.Label(gui, text="Station", font=('Angsana New',15,'bold'))
l1.grid(row=0,column=0,padx=5,pady=1)

e1 = ttk.Entry(gui, textvariable=totalStation, font=('Angsana New',15,'bold'))
e1.grid(row=0,column=1,padx=5,pady=1)
 
l2 = ttk.Label(gui, text="price", font=('Angsana New',15,'bold'))
l2.grid(row=1,column=0,padx=5,pady=1)

e2 = ttk.Entry(gui, textvariable=btsPrice, font=('Angsana New',15,'bold'))
e2.grid(row=1,column=1,padx=5,pady=1)  


b1 = ttk.Button(gui, text='Calculate', command=cal)
b1.grid(row=2,column=1,padx=5,pady=1)

r1 = ttk.Label(gui, text="Result: ", font=('Angsana New',15,'bold'))
r1.grid(row=3,column=0,padx=5,pady=1)

l2 = ttk.Label(gui, textvariable=totalFare, foreground='green', font=('Angsana New',30,'bold'))
l2.grid(row=3,column=1,padx=5,pady=1)


gui.mainloop()

 