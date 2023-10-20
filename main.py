from webscrapper import ScrapEpisodes
from Algorithmie.Algorithmie import Algorithmie

scrapper = ScrapEpisodes("https://www.spin-off.fr/calendrier_des_series.html")
episodes = scrapper.getAllEpisodes()

for episode in episodes:
    print(episode)

algorithmie = Algorithmie()
diffusions_channels = algorithmie.getChaineDiffusion(episodes)
print(diffusions_channels)