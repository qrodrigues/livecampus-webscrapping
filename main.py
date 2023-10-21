from webscrapper import ScrapEpisodes
from Algorithmie.Algorithmie import Algorithmie

base_url = "https://www.spin-off.fr"

scrapper = ScrapEpisodes(base_url, "/calendrier_des_series.html")
episodes = scrapper.getAllEpisodes()

for episode in episodes:
    print(episode)

algorithmie = Algorithmie()

print('\n---- Nombre de difussion(s) par chaîne ----\n')
diffusions_channels_counter = algorithmie.countDiffusionByKey(episodes, "channel")
top_3_channels = algorithmie.getTop3(diffusions_channels_counter, 3)
print(diffusions_channels_counter)
print('\nTop 3 des chaînes les plus diffusées : ', top_3_channels)

print('\n---- Nombre de difussion(s) par pays ----\n')
diffusions_countries_counter = algorithmie.countDiffusionByKey(episodes, "origin_country")
top_3_countries = algorithmie.getTop3(diffusions_countries_counter, 3)
print(diffusions_countries_counter)
print('\nTop 3 des pays les plus diffusées : ', top_3_countries)

print('\n---- 10 mots les plus présents dans les noms de séries ----')
top_10_words = algorithmie.getTopSeriesWords(episodes, 10)
for index, word in enumerate(top_10_words):
    print(f"{index + 1} - \"{word[0]}\" utilisé {word[1]} fois.")

print('\n----  La chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs ----')
chaine_consecutive = scrapper.findLongestConsecutiveDays(episodes)
print(f"La chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs est {chaine_consecutive[0]} avec {chaine_consecutive[1]} diffusions.")