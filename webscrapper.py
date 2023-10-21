import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class ScrapEpisodes:
    def __init__(self, base_url, url):
        self.base_url = base_url
        self.url = base_url + url
        
    def getSourceCode (self, url) :
        response = requests.get(url)
        code_source = response.text
        return BeautifulSoup(code_source, "html")

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

                    # Ajout de la durée si c'est la chaine et Apple TV+
                    duration = None
                    if channel == 'Apple TV+':
                        print('Récupération des données de la page ' + series_name + '...')
                        duration = self.getEpisodeDuration(self.base_url, '/' + episode_url)
                        time.sleep(1) # Attente d'une seconde pour ne pas spam le serveur web

                    episodes.append({
                        "air_date": str(date),
                        "origin_country": str(origin_country),
                        "channel": str(channel),
                        "series_name": str(series_name),
                        "episode_number": int(episode_number),
                        "season_number": int(season_number),
                        "episode_url": str(episode_url),
                        "duration": duration
                        })
                    
        return episodes
    
    def getEpisodeDuration (self, base_url, episode_url):
        url = base_url + episode_url
        page = self.getSourceCode(url)
        duration = page.find("div", class_="episode_infos_episode_format").text.split('minutes')[0]
        return int(duration)
    
    def findLongestConsecutiveDays(self, episodes):
        max_consecutive_days = 0
        current_consecutive_days = 0
        current_channel = None
        previous_date = None
        result = None

        for episode in episodes:
            air_date = episode.get('air_date')
            channel = episode.get('channel')

            if previous_date is not None:
                current_date = datetime.strptime(air_date, '%d-%m-%Y')

                if (current_date - previous_date).days == 1 and current_channel == channel:
                    current_consecutive_days += 1
                else:
                    current_consecutive_days = 1

                if current_consecutive_days > max_consecutive_days:
                    max_consecutive_days = current_consecutive_days
                    result = (current_channel, max_consecutive_days)

            current_channel = channel
            previous_date = datetime.strptime(air_date, '%d-%m-%Y')

        return result