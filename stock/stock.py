from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook



import csv

 
def writedata(pd,pc,qt):
	with open('data2.csv','a',newline='') as f:
		fw = csv.writer(f)
		dt = [pd,pc,qt]
		fw.writerow(dt)
		print('data was written')

def readdata():
	with open('data2.csv', newline='') as f:
		fr = csv.reader(f)
		#fw = csv.writer(f)
		#print(type(fr))
		for i,j,k in fr:
			print('product: {} price: {:.2f} quantity: {}'.format(i,float(j),k))

gui = Tk()
gui.geometry('400x400+50+50')


menubar = Menu(gui)

menufile = Menu(menubar, tearoff=0)
menufile.add_command(label='Exit', command=gui.quit)
menubar.add_cascade(label='File', menu=menufile)

menudata = Menu(menubar, tearoff=0)
menudata.add_command(label='Read CSV', command=readdata)
menubar.add_cascade(label='Data', menu=menudata)


gui.config(menu=menubar)


#----------------------tab menu-----------------------
Tab = Notebook(gui)
Fproduct = Frame(Tab)
Fproductlist = Frame (Tab)
Fstock = Frame(Tab)

iconpd = PhotoImage(file='p1.png')
iconpl = PhotoImage(file='p2.png')
iconst = PhotoImage(file='p3.png')

Tab.add(Fproduct,image=iconpd, text='Add Product', compound='left')
Tab.add(Fproductlist,image=iconpl, text='Product List', compound='left')
Tab.add(Fstock,image=iconst, text='Stock',compound='left')

#Tab.grid(row=0,column=0)
Tab.pack(fill=BOTH,expand=1)


add_product_text = ['Code','Product', 'Price','Quantity']

for j,i in enumerate(add_product_text):
	#print(j,i)
	l1 = ttk.Label(Fproduct, text=i, font=('Angsana New', 16))
	l1.grid(row=j,column=0,padx=5,pady=5,sticky=W)

ent_code = StringVar()
ent_product  = StringVar()
ent_price = StringVar()
ent_quantity = StringVar()
result  = StringVar()

def FEproduct(event):
	Eproduct.focus()

def addProduct(event=None):
	cd = ent_code.get()
	pd = ent_product.get()
	try:
		pc = float(ent_price.get())
		qt = float(ent_quantity.get())
		total = pc*qt
		result.set("code={},product={},price={:.4f},quantity={:.4f}\ntotal={:,.2f}".format(cd,pd,pc,qt,total))	 
		ent_code.set('')
		ent_product.set('')
		ent_price.set('')
		ent_quantity.set('') 
		Ecode.focus()
		writedata(pd,pc,qt)

	except ValueError:
		messagebox.showerror('error number','erorrrrrrrrrrrrrr')
		ent_price.set('')
		ent_quantity.set('')


Ecode= ttk.Entry(Fproduct, textvariable=ent_code, font=('Angsana New', 16), width=30)
Ecode.grid(row=0, column=1,padx=5,pady=5, sticky=W)


Eproduct= ttk.Entry(Fproduct, textvariable=ent_product , font=('Angsana New', 16), width=30)
Eproduct.grid(row=1, column=1,padx=5,pady=5, sticky=W)

Eprice= ttk.Entry(Fproduct, textvariable=ent_price, font=('Angsana New', 16), width=30)
Eprice.grid(row=2, column=1,padx=5,pady=5, sticky=W) 

Equantity= ttk.Entry(Fproduct, textvariable=ent_quantity, font=('Angsana New', 16), width=30)
Equantity.grid(row=3, column=1,padx=5,pady=5, sticky=W)
Equantity.bind('<Return>', addProduct)

BaddProduct = ttk.Button(Fproduct, text='Add Product', command=addProduct)
BaddProduct.grid(row=4, column=1,padx=5,pady=5,ipady=10, ipadx=50, sticky=W)

Result = ttk.Label(Fproduct,textvariable=result, font=('Angsana New', 16), width=70)
Result.grid(row=5, column=1,padx=5,pady=5,ipady=10)

Ecode.focus()

gui.mainloop()