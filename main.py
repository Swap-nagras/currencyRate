from bs4 import BeautifulSoup
import requests
def get_curency(from_currency, to_currency):
    url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    return rate

from_currency="USD"
to_currency="INR"
current_rate=get_curency(from_currency, to_currency)
print(f'1 {from_currency} is {current_rate}.\nThank you for visiting us.')

