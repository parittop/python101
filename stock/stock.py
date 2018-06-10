from tkinter import *
from tkinter import ttk
from tkinter import messagebox




gui = Tk()
gui.geometry('400x400+50+50')

add_product_text = ['Code','Product', 'Price','Quantity']

for j,i in enumerate(add_product_text):
	print(j,i)
	l1 = ttk.Label(gui, text=i, font=('Angsana New', 16))
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
	except ValueError:
		messagebox.showerror('error number','erorrrrrrrrrrrrrr')
		pc = 0
		ent_price.set('')
	try:	
		qt = float(ent_quantity.get())
	except ValueError:
		qt=0
		ent_quantity.set('')

	total = pc*qt
	result.set("code={},product={},price={:.4f},quantity={:.4f}\ntotal={:,.2f}".format(cd,pd,pc,qt,total))
	 
	ent_code.set('')
	ent_product.set('')
	ent_price.set('')
	ent_quantity.set('') 
	Ecode.focus()

Ecode= ttk.Entry(gui, textvariable=ent_code, font=('Angsana New', 16), width=30)
Ecode.grid(row=0, column=1,padx=5,pady=5, sticky=W)


Eproduct= ttk.Entry(gui, textvariable=ent_product , font=('Angsana New', 16), width=30)
Eproduct.grid(row=1, column=1,padx=5,pady=5, sticky=W)

Eprice= ttk.Entry(gui, textvariable=ent_price, font=('Angsana New', 16), width=30)
Eprice.grid(row=2, column=1,padx=5,pady=5, sticky=W) 

Equantity= ttk.Entry(gui, textvariable=ent_quantity, font=('Angsana New', 16), width=30)
Equantity.grid(row=3, column=1,padx=5,pady=5, sticky=W)
Equantity.bind('<Return>', addProduct)

BaddProduct = ttk.Button(gui, text='Add Product', command=addProduct)
BaddProduct.grid(row=4, column=1,padx=5,pady=5,ipady=10, ipadx=50, sticky=W)

Result = ttk.Label(gui,textvariable=result, font=('Angsana New', 16), width=70)
Result.grid(row=5, column=1,padx=5,pady=5,ipady=10)

Ecode.focus()

gui.mainloop()