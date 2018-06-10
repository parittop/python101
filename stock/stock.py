from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook

import stockchecker

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
		#try: 
		for i in treeview2.get_children():
			treeview2.delete(i)
		#except:
		#	pass
		for i,j,k in fr:
			#print('product: {} price: {:.2f} quantity: {}'.format(i,float(j),k))
			tv_data = [i,j,k]
			treeview2.insert('','end',values=tv_data)

gui = Tk()
gui.geometry('400x400+50+50')
gui.title('My Python App')
gui.state('zoomed')

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

treeview1 = ttk.Treeview(Fproductlist, height=5)
treeview1.pack(fill=BOTH,expand=1)
 
treeview1.insert('','0','water',text='Water')
treeview1.insert('','1','softdrink',text='Softdrink')
treeview1.insert('','2','juice',text='juice') 

treeview1.insert('water','0','aura', text='Aura')
treeview1.insert('aura','end','sub-aura', text='Sub-Aura')
treeview1.insert('softdrink','0','softdrink1',text='Softdrink1')

 
collist = ['Product','Price']
treeview2 = ttk.Treeview(Fproductlist, columns=collist, show='headings', height=10)
treeview2.pack(fill=X)

for col in collist:
	treeview2.heading(col, text=col.title())

#------------Insert data---------------
 
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

def getstock():
	ptt = PTTValue.get()
	scb = SCBValue.get()
	#print(ptt,scb)
	 
	disp = []
	if ptt=='1': 
		stockname,stockprice = stockchecker.checkprice('PTT')
		#print(stockname,stockprice)
		#disp.append('Stock: '+stockname + ' Price: '+ stockprice)
		r=[stockname,stockprice]
		disp.append(r)
	if scb=='1': 
		stockname,stockprice = stockchecker.checkprice('SCB')
		#print(stockname,stockprice)
		#disp.append('Stock: '+stockname + ' Price: '+ stockprice)
		r=[stockname,stockprice]
		disp.append(r)
	print(disp)

	for i in treeview3.get_children():
			treeview3.delete(i)
	 
	for i in disp:		 
		treeview3.insert('','end',values=i)


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

PTTValue = StringVar()
SCBValue = StringVar()

F2stock = LabelFrame(Fstock, text='Criteria', )
F2stock.grid(row=0,column=0,sticky=(W,E))

CB = ttk.Checkbutton(F2stock,text='PTT',variable=PTTValue)
CB.grid(row=0,column=0)

CB2 = ttk.Checkbutton(F2stock,text='SCB',variable=SCBValue)
CB2.grid(row=1,column=0)

Bstock = ttk.Button(F2stock,text='Get Price', command=getstock)
Bstock.grid(row=2,column=0)

stockcollist = ['Stock','Price']
treeview3 = ttk.Treeview(Fstock, columns=stockcollist, show='headings', height=10)
treeview3.grid(row=1,column=0)
 

for col in stockcollist:
	treeview3.heading(col, text=col.title())

radio= StringVar()
rb1 = ttk.Radiobutton(F2stock,text='PTT', variable=radio, value=1)
rb1.grid(row=0,column=1)

LB1 = LabelFrame(Fstock,text='Dropdown')
LB1.grid(row=2,column=0)

drop=['PTT','SCB','TMB','AOT']
combo = ttk.Combobox(LB1, values=drop)
combo.grid(row=0,column=0)
combo.set('SCB')
gui.mainloop()