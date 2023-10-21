from webscrapper import ScrapEpisodes
from Algorithmie.Algorithmie import Algorithmie
from ManagerCSV.ManagerCSV import ManagerCSV

scrapper = ScrapEpisodes("https://www.spin-off.fr/calendrier_des_series.html")
episodes = scrapper.getAllEpisodes()

for episode in episodes:
    print(episode)

algorithmie = Algorithmie()
diffusions_channels_counter = algorithmie.countDiffusionByKey(episodes, "channel")
top_3_channels = algorithmie.getTop3(diffusions_channels_counter, 3)

diffusions_countries_counter = algorithmie.countDiffusionByKey(episodes, "origin_country")
top_3_countries = algorithmie.getTop3(diffusions_countries_counter, 3)

print('\n---- Nombre de difussion(s) par chaîne ----\n')
print(diffusions_channels_counter)
print('\nTop 3 des chaînes les plus diffusées : ', top_3_channels)

print('\n---- Nombre de difussion(s) par pays ----\n')
print(diffusions_countries_counter)
print('\nTop 3 des pays les plus diffusées : ', top_3_countries)


print('\n---- Gestion du CSV ---- \n')
csv_manager = ManagerCSV(episodes)
csv_df = csv_manager.data_to_df()
csv_manager.df_to_csv(csv_df,"../data/files/episodes.csv")
csv_tuples = csv_manager.csv_to_tuples("../data/files/episodes.csv")
csv8types = csv_manager.verify_types(csv_tuples)

# print('\n- Affichage des types des tuples : \n',csv8types)