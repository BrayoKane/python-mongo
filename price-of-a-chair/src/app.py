import requests
from bs4 import BeautifulSoup #screen-scraping library


#request = requests.get("http://www.google.com")
request = requests.get("https://www.johnlewis.com/house-by-john-lewis-curve-dining-chair-white/p231441579")
content = request.content #getting content of the page
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span",{"itemprop":"price","class":"now-price"}) #dictionary
#print(element.text.strip())
string_price = element.text.strip() #"#£19.00"

price_without_symbol = string_price[1:]

price = (float(price_without_symbol))

if price < 50:
    print("You should buy the chair!")
    print("The current price is {}.".format(string_price))
else:
    print("Don't buy the chair!!")



# <span itemprop="price" class="now-price"> £19.00 </span>

#print(request.content)
