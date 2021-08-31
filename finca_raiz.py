from requests_html import HTMLSession
import pandas as pd
import time

url = 'https://www.fincaraiz.com.co/apartamentos/venta/bogota?usado=true&pagina=1'
s = HTMLSession()
finca_r = []

def request(url):
    r = s.get(url)
    r.html.render(sleep = 1)
    return r.html.xpath('//*[@id="listingContainer"]', first = True)

def parse(products):
    for item in products.absolute_links :
        r = s.get(item)
        try:
            name = r.html.find('div.MuiBox-root header div p',first = True).text
            barrio = r.html.find('div.MuiBox-root header div p:nth-of-type(2)',first = True).text
            description = r.html.find('div.MuiCollapse-wrapper div p',first = True).text
            precio = r.html.find('div:nth-of-type(3) aside div div:nth-of-type(1) div:nth-of-type(1) div div p:nth-of-type(2)',first = True).text
            codigo = r.html.find('*#general div div:nth-of-type(1) div div div p:nth-of-type(2)',first = True).text
        except:
            name = 'None'
            barrio = 'None'
            description = 'None'
            precio = 'None'
            codigo = 'None'
        
        try:
            attrData_1 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(1)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    attrValue = attrValue.strip()    
                attrData_1[attrLabel] = attrValue
        except:
            attrData_1 = 'None'
        
        try:
            attrData_2 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div.MuiBox-root.jss284.jss249.jss246',first = True).text:
                attrLabel = r.html.find('div.MuiBox-root.jss284.jss249.jss246 div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div.MuiBox-root.jss284.jss249.jss246 div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    attrValue = attrValue.strip()    
                attrData_2[attrLabel] = attrValue
        except:
            attrData_2 ='None'
        
        try:
            attrData_3 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(3)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(3) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(3) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    attrValue = attrValue.strip()    
                attrData_3[attrLabel] = attrValue
        except:
            attrData_3 = 'None'
        
        try:
            attrData_4 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(3)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(3) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(3) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    attrValue = attrValue.strip()    
                attrData_4[attrLabel] = attrValue
        except:
            attrData_4 = 'None'

        try:
            attrData_5 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(4)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(4) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(4) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    attrValue = attrValue.strip()    
                attrData_5[attrLabel] = attrValue
        except:
            attrData_5 = 'None'
        
        try:
            attrData_6 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(5)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(5) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(5) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    attrValue = attrValue.strip()    
                attrData_6[attrLabel] = attrValue
        except:
            attrData_6 = 'None'
        
        try:
            attrData_7 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(6)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(6) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(6) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    arrtvalue = attrValue.replace(u"\xa0","")
                    attrValue = attrValue.strip()    
                attrData_7[attrLabel] = attrValue
        except:
            attrData_7 = 'None'
        
        try:
            attrData_8 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(7)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(7) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()

                attrValue = r.html.find('div:nth-of-type(7) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    arrtvalue = attrValue.replace(u"\xa0","")
                    attrValue = attrValue.strip()    
                attrData_8[attrLabel] = attrValue
        except:
            attrData_8 = 'None'

        try:
            attrData_9 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(8)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(8) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()
                attrValue = r.html.find('div:nth-of-type(8) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    arrtvalue = attrValue.replace(u"\xa0","")
                    attrValue = attrValue.strip()    
                    attrData_9[attrLabel] = attrValue
        except:
            attrData_9 = 'None'

        try:
            attrData_10 = {}
            for attrs in r.html.find('*#general div div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(9)',first = True).text:
                attrLabel = r.html.find('div:nth-of-type(9) div:nth-of-type(2) p:nth-of-type(1)',first = True).text
                if attrLabel is not None:
                    attrLabel = attrLabel.replace(u"\n","")
                    attrLabel = attrLabel.replace(u"\t","")
                    attrLabel = attrLabel.strip()
                attrValue = r.html.find('div:nth-of-type(9) div:nth-of-type(2) p:nth-of-type(2)',first = True).text
                if attrValue is not None:
                    attrValue = attrValue.replace(u"\n","")
                    attrValue = attrValue.replace(u"\t","")
                    arrtvalue = attrValue.replace(u"\xa0","")
                    attrValue = attrValue.strip()    
                    attrData_10[attrLabel] = attrValue
        except:
            attrData_10 = 'None'
        
        apto = {
            'name' : name,
            'barrio' : barrio,
            'descripcion' : description,
            'precio': precio,
            'codigo': codigo,
            'opt1' : attrData_1,
            'opt2' : attrData_2,
            'opt3' : attrData_3,
            'opt4' : attrData_4,
            'opt5' : attrData_5,
            'opt6' : attrData_6,
            'opt7' : attrData_7,
            'opt8' : attrData_8,
            'opt9' : attrData_9,
            'opt10' : attrData_10
        }
        finca_r.append(apto)

def output():
    df = pd.DataFrame(finca_r)
    df.to_csv('finca_raiz_demo.csv', index = False)
    print('Saved to CSV file')

x = 1
while True:
    try:
        products = request(f'https://www.fincaraiz.com.co/apartamentos/venta/bogota?usado=true&pagina={x}')
        print(f'Getting items from page {x}')
        parse(products)
        print('Total Items:',len(finca_r))
        x = x + 1
        time.sleep(2)
    except:
        print('¡No more items!')
        break
output()
