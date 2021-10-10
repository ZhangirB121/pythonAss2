from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver

class ParseArticle:
    def collectingInform(self,nameOfCurrency):

        URL='https://coinmarketcap.com/currencies/'+nameOfCurrency+'/news/'
        r = requests.get(URL, 'html.parser').text
        soup= BeautifulSoup(r,'lxml')
        header=soup.h2.text
        print(header,'\n')
        allOfTheText=soup.text.strip()
        ct=0
        for i in range(len(allOfTheText)):
            print(allOfTheText[i],end='')
            if allOfTheText[i]==' ':
                ct+=1
            if ct==5:
                print('\n',end='')
                ct=0
        print()