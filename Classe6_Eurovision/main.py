###
# pip install beautifulsoup4                #
# pip install requests                      #
# pip install spotipy                       #
# pip install lxml                          #
# pip install openpyxl                      #
#############################################

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

rango = range(2000, 2024, 1)

def extract_wiki(rango):
    for r in rango:
        try:
            resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_2023")
            codi_web = resposta.text

            soup = BeautifulSoup(codi_web, 'html.parser')
            final = soup.find('span', id="Final")
            tabla = final.find_next("table")
            df = pd.read_html(str(tabla))[0]

            print(df)
            df.to_excel(f"final-{r}.xlsx", index=False)
            print(f"todo bien en {r}")
            time.sleep(1)
        except AttributeError:
            print(f"problema en {r}")

extract_wiki(rango)
