import requests
from bs4 import BeautifulSoup

url=requests.get('https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx')

def scrappingTipoCambio():
    if(url.status_code==200):
        html=BeautifulSoup(url.text,'html.parser')
        tabla=html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
        print(tabla)
    else:
        print('error '+str(url.status_code))

if __name__=="__main__":
    scrappingTipoCambio()