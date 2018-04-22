import lxml
from lxml import html
import requests

url = raw_input('Enter a URL: ')
response = requests.get(url)

if (response.status_code == 200):
    pagehtml = html.fromstring(response.text)

    news1 = pagehtml.xpath('//h1[@class="story-body__h1"]/text()')
    news2 = pagehtml.xpath('//p[@class="story-body__introduction"]/text()')
print("\n".join(news1) + " (BBC News)")
print("\n".join(news2))

