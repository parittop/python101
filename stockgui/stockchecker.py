from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup

def checkprice(stockcode):

	url='http://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol='+stockcode+'&ssoPageId=10&selectPage=2'

	webopen= req(url)
	page_html = webopen.read()
	webopen.close()

	#print(page_html)

	stockweb = soup(page_html,'html.parser')
	#print(stockweb)
	data=stockweb.findAll('div', {'class':'col-xs-6'})

	#print('Line ', data[2].text)
	stockname = data[0].text
	stockprice = data[2].text

	#print('Stock: {} Price: {:,.4f}'.format(stockname,float(stockprice)))
	return (stockname, stockprice)


#checkprice('HANA')
#x,y = checkprice('TMB')
#print(x)
#print(y)