import requests
from bs4 import BeautifulSoup as bs 
#pip install bs4
pagina = requests.get(
         'http://beans.itcarlow.ie/prices-loyalty.html')
sopa = bs (pagina.text, 'html.parser')
print (sopa.strong.string)
print (sopa.h2)
#notebook CMD > pip install requests
#+ loyalty 
#pode colocar qualquer pagina
