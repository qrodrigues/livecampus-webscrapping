from webscrapper import ScrapEpisodes
from Algorithmie.Algorithmie import Algorithmie
from ManagerCSV.ManagerCSV import ManagerCSV

base_url = "https://www.spin-off.fr"
url = "/calendrier_des_series.html" + "?date=2023-10" # ?date=2023-10 n'est pas obligatoire mais il permet d'assurer le mois d'octobre.

scrapper = ScrapEpisodes(base_url, url)
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


print('\n---- Gestion du CSV : Traitement ... ---- \n')
csv_manager = ManagerCSV(episodes)
csv_df = csv_manager.data_to_df()
csv_manager.df_to_csv(csv_df,"./data/files/episodes.csv")


print('\n- Affichage des tuples depuis le CSV : \n')
csv_tuples = csv_manager.csv_to_tuples("./data/files/episodes.csv")
for tup in csv_tuples : 
    print(tup)

print('\n- Affichage des types des tuples : \n')
csv_types = csv_manager.verify_types(csv_tuples)
for typ in csv_types : 
    print(typ)
    
print('\n---- Gestion du CSV : Fin du traitement ... ---- \n')

print('\n---- 10 mots les plus présents dans les noms de séries ----')
top_10_words = algorithmie.getTopSeriesWords(episodes, 10)
for index, word in enumerate(top_10_words):
    print(f"{index + 1} - \"{word[0]}\" utilisé {word[1]} fois.")

print('\n----  La chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs ----')
chaine_consecutive = algorithmie.findLongestConsecutiveDays(episodes)
print(f"La chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs est {chaine_consecutive[0]} avec {chaine_consecutive[1]} diffusions.")