import re
import requests
from bs4 import BeautifulSoup
import json


class Scrape:
    
    items={"hotels":{"website":"https://takhfifan.com/global/%D8%AA%D8%AE%D9%81%DB%8C%D9%81%D8%A7%D9%86%20%D9%87%D8%A7%DB%8C%20%D9%85%D8%B3%D8%A7%D9%81%D8%B1%D8%AA%DB%8C"},"main":{"website":"https://takhfifan.com/"}}

    def change(self,item):
        img=item.attrs["data-src"]
        url='https://takhfifan.com'+item.parent.parent.attrs['href']
        text=(re.sub('(\n+|\s+)',' ',item.parent.nextSibling.find('strong').text)).strip()
        darsad=item.parent.nextSibling.find('span',attrs={"class":"deal-discount-number"}).text
        now=item.parent.nextSibling.find('span',attrs={"class":"deal-price-number number-font"}).text
        before=(re.sub(r'\n','',(item.parent.nextSibling.find('div',attrs={"class":"deal-retail-price line-through number-font"}).text))).strip()
        return ({"img":img,'url':url,"text":text,"darsad":darsad,"now":now,"before":before})


    def __init__(self):
        title=input('please enter title: ')
        result=requests.get(((self.items)[title])['website'])
        content=BeautifulSoup(result.text,'html.parser')
        allimages=(content.find('div',attrs={"class":"deals three-col clear lazy-parent"})).findAll('img',attrs={"class":"lazy"})
        print(len(allimages))
        lastResult=list(map(self.change,allimages))
        print(lastResult)

    
        
Scrape()
