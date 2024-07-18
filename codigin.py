


import pyautogui as pa
import pandas as pd
import time

#from pandas import read_csv
#from time import sleep
#sleep(5)

pa.PAUSE = 0.5

pa.press('win')
pa.write('chrome')
pa.press('enter')

time.sleep(2)
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pa.press('enter')

time.sleep(3)
pa.click(x=414, y=408)

pa.write('email@gamil.com')
pa.press('tab')
pa.write('senha')
pa.press('tab')
pa.press('enter')


tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:

    pa.click(x=427, y=293)
    pa.write(str(tabela.loc[linha, 'codigo']))
    pa.press('tab')

    pa.write(str(tabela.loc[linha, 'marca']))
    pa.press('tab')

    pa.write(str(tabela.loc[linha, 'tipo']))
    pa.press('tab')

    pa.write(str(tabela.loc[linha, 'categoria']))
    pa.press('tab')

    pa.write(str(tabela.loc[linha, 'preco_unitario']))
    pa.press('tab')

    pa.write(str(tabela.loc[linha, 'custo']))
    pa.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    
    if obs != 'nan':
        pa.write(obs)

    pa.press('tab')
    pa.press('enter')

    pa.scroll(5000)

