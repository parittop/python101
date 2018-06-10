from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

stockcode = input('Please input stock quote: ')
url = 'http://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol='+stockcode+'&ssoPageId=9&selectPage='
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

price = page_soup.findAll("div",{"class":"col-xs-6 col-xs-offset-6 colorGreen"})

print(stockcode + ' Last Price is ' + price[0].text.strip())


                            
