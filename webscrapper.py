import requests
from bs4 import BeautifulSoup

class ScrapEpisodes:
    def __init__(self, url):
        self.url = url
        
    def getSourceCode (self, url) :
        response = requests.get(url)
        code_source = response.text
        return BeautifulSoup(code_source, "html")
        
    # def getAllEpisodes (self):
    #     episodes = []
    #     source_code = self.getSourceCode(self.url)
    #     jours_tag = source_code.find_all('td', class_="td_jour")
    #     for jour in jours_tag:
    #         if jour.find("div", {"class": ["div_jour", "div_jourcourant"]}): # si il a un enfant div_jour (pour vérifier si il est pas vide)
    #             date = ""
    #             pays = []
    #             chaines = []
    #             noms = []
    #             numeros_episodes = []
    #             numeros_saisons = []
    #             links = []

    #             div_jours_tag = jour.find("div", {"class": ["div_jour", "div_jourcourant"]})
    #             date = div_jours_tag["id"].split("jour_")[1]
    #             pays_chaines = jour.find_all("img")
    #             for i in range(len(pays_chaines)):
    #                 if i % 2 == 0:
    #                     pays.append(pays_chaines[i].get("alt"))
    #                 else:
    #                     chaines.append(pays_chaines[i].get("alt"))
    #             nom_numeros = jour.find_all("span", class_="calendrier_episodes")
    #             for nom_numero in nom_numeros:
    #                 noms.append(nom_numero.find("a").text)
    #                 links.append(nom_numero.find("a")["href"])
    #                 numeros = nom_numero.find_all("a")[1].text
    #                 numeros_saisons.append(numeros.split('.')[0])
    #                 numeros_episodes.append(numeros.split('.')[1])
                   
    #             # Parsing dans un objet episode
    #             for x in range(len(noms)):
    #                 episodes.append((date, pays[x], chaines[x], noms[x], numeros_episodes[x], numeros_saisons[x], links[x]))
            
    #     return episodes

    def getAllEpisodes (self):
        episodes = []
        page = self.getSourceCode(self.url)
        td_tags = page.find_all("td", class_="td_jour")

        spans = page.find_all("span", class_="calendrier_episodes")

        for td in td_tags:
            div_jour_tag = td.find("div", class_="div_jour")
            if div_jour_tag:
                date = div_jour_tag["id"].split("jour_")[1]
                span_tags = td.find_all("span", class_="calendrier_episodes")
                for span in span_tags:
                    series_name = span.find("a").text
                    numbers = span.find_all("a")[1].text.split(".")
                    season_number = numbers[0]
                    episode_number = numbers[1]
                    channel = span.find_previous_sibling("img")['alt']
                    channel_tag = span.find_previous_sibling("img")
                    country_tag = channel_tag.find_previous_sibling("img")
                    origin_country = country_tag['alt']
                    episode_url = span.find("a").find_next("a")["href"]
                    episodes.append({
                        "air_date": str(date),
                        "origin_country": str(origin_country),
                        "channel": str(channel),
                        "series_name": str(series_name),
                        "episode_number": int(episode_number),
                        "season_number": int(season_number),
                        "episode_url": str(episode_url)
                        })
        return episodes