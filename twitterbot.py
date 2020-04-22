import  requests
import json
import time

from bs4 import BeautifulSoup


while 1:
    page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
    soup = BeautifulSoup(page.text, 'html.parser')
    container = soup.findAll("div", {"class": "maincounter-number"})

    cases = container[0].text.strip()
    mortes = container[1].text.strip()
    recuperados = container[2].text.strip()

    #print(cases)
    #print(mortes)
    #print(recuperados)

    brasil = ("Total de casos Corona Vírus no Brasil: \n" + \
                "Casos Confirmados:" +cases+ "\n" + \
                "Óbitos: "+ mortes+ "\n"+ \
                "Recuperados: " +recuperados + "\n\n"
                    )

    page = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(page.text, 'html.parser')
    container = soup.findAll("div", {"class": "maincounter-number"})
    cases = container[0].text.strip()
    mortes = container[1].text.strip()
    recuperados = container[2].text.strip()
    mundo = ("Total de casos Corona Vírus no Mundo: \n" + \
                "Casos Confirmados:" +cases+ "\n" + \
                "Óbitos: "+ mortes+ "\n"+ \
                "Recuperados: " +recuperados + "\n\n"
                    )

    print(brasil)
    print(mundo)

    url = "https://hooks.zapier.com/hooks/catch/7317593/o5fx7n7/"
    data ={'Value1': brasil, 'Value2': mundo}
    headers= {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r= requests.post(url, data=json.dumps(data), headers=headers)
    print(r.text)
    print("dormindo")
    time.sleep(3600)