from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
html_text = requests.get('https://www.zomato.com/ncr/khabootar-dlf-phase-4-gurgaon/order', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
datas = soup.find_all('div', class_='sc-1s0saks-17 bGrnCu')

filename = 'products.csv'
f = open(filename, 'w', encoding="utf-8")

title = 'Item_Name,Item_Description,Item_Price,Must_Try\n'
f.write(title)

for data in datas:
    item_name = data.find('h4', class_='sc-1s0saks-15 iSmBPS').text
    item_desc = data.find('p', class_='sc-1s0saks-12 hcROsL').text.replace('... read more', '').replace(',', '')
    item_pri = data.find('span', class_='sc-17hyc2s-1 cCiQWA').text
    if data.find('div', class_='sc-2gamf4-0 cRxPpO') is not None:
        item_try = True
    else:
        item_try = False

    print(item_name+','+item_desc+','+item_pri+','+str(item_try)+'\n')
    f.write(item_name + ',' + item_desc + ',' + item_pri + ',' + str(item_try) + '\n')

f.close()
