import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.ttk import Treeview

ANCHO=640
ALTO=480

url=requests.get('https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx')

class TipoCambio:
    def __init__(self,window):
        self.wind=window
        self.wind.title("Tipos de Cambio")
        self.wind.geometry(str(ANCHO)+'x'+str(ALTO))
        self.wind.configure(bg='#49A')

        #Boton Importar
        btnImportar=Button(text='Importar tipos de cambio',command=self.scrappingTipoCambio)
        btnImportar.grid(row=0,column=1,columnspan=1,sticky=W+E)

        #Treeview
        self.trvTipoCambio=Treeview(height=8,columns=('#1','#2'))
        self.trvTipoCambio.grid(row=2,column=0,columnspan=3,padx=10)
        self.trvTipoCambio.heading('#0',text='Moneda',anchor=CENTER)
        self.trvTipoCambio.heading('#1',text='Compra',anchor=CENTER)
        self.trvTipoCambio.heading('#2',text='Venta',anchor=CENTER)

    def scrappingTipoCambio(self):
        tiposCambio=[]
        if(url.status_code==200):
            html=BeautifulSoup(url.text,'html.parser')
            tabla=html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
            for i in range(7):
                fila=html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(i)})
                moneda=fila.find('td',{'class':'APLI_fila3'})
                valores=fila.find_all('td',{'class':'APLI_fila2'})
                dictMoneda={
                    'moneda':moneda.get_text(),
                    'compra':valores[0].get_text(),
                    'venta':valores[1].get_text(),
                }
                tiposCambio.append(dictMoneda)
                self.trvTipoCambio.insert('',END,text=moneda.get_text(),values=[valores[0].get_text(),valores[1].get_text()])

        else:
            print('error '+str(url.status_code))

if __name__=="__main__":
    window=Tk()
    app=TipoCambio(window)
    window.mainloop()