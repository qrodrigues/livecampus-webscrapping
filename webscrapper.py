import requests
from bs4 import BeautifulSoup

class ScrapEpisodes:
    def __init__(self, url):
        self.url = url
        
    def getSourceCode (self, url) :
        response = requests.get(url)
        code_source = response.text
        return BeautifulSoup(code_source, "html")
        
    def getAllEpisodes (self):
        episodes = []
        source_code = self.getSourceCode(self.url)
        jours_tag = source_code.find_all('td', class_="td_jour")
        for jour in jours_tag:
            if jour.find("div", {"class": ["div_jour", "div_jourcourant"]}): # si il a un enfant div_jour (pour vérifier si il est pas vide)
                date = ""
                pays = []
                chaines = []
                noms = []
                numeros_episodes = []
                numeros_saisons = []
                links = []

                div_jours_tag = jour.find("div", {"class": ["div_jour", "div_jourcourant"]})
                date = div_jours_tag["id"].split("jour_")[1]
                pays_chaines = jour.find_all("img")
                for i in range(len(pays_chaines)):
                    if i % 2 == 0:
                        pays.append(pays_chaines[i].get("alt"))
                    else:
                        chaines.append(pays_chaines[i].get("alt"))
                nom_numeros = jour.find_all("span", class_="calendrier_episodes")
                for nom_numero in nom_numeros:
                    noms.append(nom_numero.find("a").text)
                    links.append(nom_numero.find("a")["href"])
                    numeros = nom_numero.find_all("a")[1].text
                    numeros_saisons.append(numeros.split('.')[0])
                    numeros_episodes.append(numeros.split('.')[1])
                   
                # Parsing dans un objet episode
                for x in range(len(noms)):
                    episodes.append((date, pays[x], chaines[x], noms[x], numeros_episodes[x], numeros_saisons[x], links[x]))
            
        return episodes